// Webhook da Hotmart: recebe o aviso de compra/reembolso/chargeback e libera (ou revoga)
// o acesso do aluno à certificação correspondente no Firestore do app de simulados.
// Roda como função serverless na Vercel (grátis) para não exigir o plano pago do Firebase.
const admin = require("firebase-admin");

function getAdmin() {
  if (!admin.apps.length) {
    const json = Buffer.from(process.env.FIREBASE_SERVICE_ACCOUNT_BASE64, "base64").toString("utf8");
    admin.initializeApp({ credential: admin.credential.cert(JSON.parse(json)) });
  }
  return admin;
}

const GRANT_EVENTS = new Set(["PURCHASE_APPROVED", "PURCHASE_COMPLETE"]);
const REVOKE_EVENTS = new Set([
  "PURCHASE_CANCELED",
  "PURCHASE_REFUNDED",
  "PURCHASE_CHARGEBACK",
  "PURCHASE_EXPIRED",
  "SUBSCRIPTION_CANCELLATION",
]);

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.status(405).json({ error: "method not allowed" });
    return;
  }

  // A Hotmart envia o "Hottok" (token configurado no painel de webhook) para autenticar a chamada.
  const hottok = req.body?.hottok || req.query?.hottok;
  if (!process.env.HOTMART_HOTTOK || hottok !== process.env.HOTMART_HOTTOK) {
    res.status(401).json({ error: "invalid hottok" });
    return;
  }

  const event = req.body?.event;
  const email = req.body?.data?.buyer?.email;
  const productId = String(req.body?.data?.product?.id || "");
  const productName = req.body?.data?.product?.name || "";

  if (!email || (!GRANT_EVENTS.has(event) && !REVOKE_EVENTS.has(event))) {
    res.status(200).json({ ok: true, skipped: true });
    return;
  }

  let productMap = {};
  try {
    productMap = JSON.parse(process.env.HOTMART_PRODUCT_MAP || "{}");
  } catch {
    productMap = {};
  }
  // HOTMART_PRODUCT_MAP mapeia o ID (ou nome) do produto na Hotmart para o nome exato
  // da certificação cadastrada em Certificações no painel admin. Ex: {"123456":"CPA-20"}
  const certificationName = productMap[productId] || productMap[productName];
  if (!certificationName) {
    res.status(200).json({ ok: true, skipped: true, reason: "produto não mapeado em HOTMART_PRODUCT_MAP" });
    return;
  }

  const fbAdmin = getAdmin();
  const db = fbAdmin.firestore();

  const certSnap = await db.collection("certifications").where("name", "==", certificationName).limit(1).get();
  if (certSnap.empty) {
    res.status(200).json({ ok: true, skipped: true, reason: "certificação não encontrada no Firestore" });
    return;
  }
  const certificationId = certSnap.docs[0].id;
  const grant = GRANT_EVENTS.has(event);
  const emailKey = email.toLowerCase().trim();

  try {
    const userRecord = await fbAdmin
      .auth()
      .getUserByEmail(emailKey)
      .catch(() => null);

    const certOp = grant
      ? fbAdmin.firestore.FieldValue.arrayUnion(certificationId)
      : fbAdmin.firestore.FieldValue.arrayRemove(certificationId);

    if (userRecord) {
      // Aluno já tem conta no site: libera/revoga direto no perfil dele.
      await db.collection("users").doc(userRecord.uid).set({ purchasedCertifications: certOp }, { merge: true });
    } else {
      // Comprou na Hotmart mas ainda não criou conta no site: fica pendente até o cadastro.
      await db
        .collection("pendingAccess")
        .doc(emailKey)
        .set({ certifications: certOp, updatedAt: fbAdmin.firestore.FieldValue.serverTimestamp() }, { merge: true });
    }
    res.status(200).json({ ok: true });
  } catch (err) {
    console.error("Erro ao processar webhook Hotmart:", err);
    res.status(500).json({ error: "internal error" });
  }
};
