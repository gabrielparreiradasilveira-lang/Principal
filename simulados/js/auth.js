import { auth, db } from "./firebase-config.js";
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  updateProfile,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import {
  doc,
  setDoc,
  getDoc,
  updateDoc,
  deleteDoc,
  increment,
  serverTimestamp,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

// Estado global simples do usuário logado + seu perfil (role: 'aluno' | 'admin')
export const state = {
  user: null,
  profile: null,
  ready: false,
  deviceWarning: false,
};

const DEVICE_ID_KEY = "simulados_device_id";
function getOrCreateDeviceId() {
  let id = localStorage.getItem(DEVICE_ID_KEY);
  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem(DEVICE_ID_KEY, id);
  }
  return id;
}

// Trava "leve" de dispositivo: sem Cloud Functions (Firebase plano gratuito), então isto
// não bloqueia acesso de fato — só avisa quando detecta login vindo de um dispositivo
// diferente do último registrado, e mantém uma contagem para o admin acompanhar.
async function checkDevice(uid) {
  const deviceId = getOrCreateDeviceId();
  const ref = doc(db, "users", uid);
  const snap = await getDoc(ref);
  const lastDeviceId = snap.data()?.lastDeviceId;

  if (!lastDeviceId) {
    await setDoc(ref, { lastDeviceId: deviceId, lastDeviceAt: serverTimestamp() }, { merge: true });
    state.deviceWarning = false;
    return;
  }
  if (lastDeviceId !== deviceId) {
    await updateDoc(ref, {
      lastDeviceId: deviceId,
      lastDeviceAt: serverTimestamp(),
      deviceSwitchCount: increment(1),
    });
    state.deviceWarning = true;
  } else {
    state.deviceWarning = false;
  }
}

const listeners = [];
export function onStateChange(cb) {
  listeners.push(cb);
  if (state.ready) cb(state);
}
function notify() {
  listeners.forEach((cb) => cb(state));
}

export async function signup(name, email, password) {
  const cred = await createUserWithEmailAndPassword(auth, email, password);
  await updateProfile(cred.user, { displayName: name });

  // Se a Hotmart (ou o admin manualmente) já liberou acesso para este e-mail antes do
  // cadastro, o webhook deixou um registro em pendingAccess/{email} — aplica aqui.
  const pendingRef = doc(db, "pendingAccess", email.toLowerCase().trim());
  const pendingSnap = await getDoc(pendingRef);
  const purchasedCertifications = pendingSnap.exists() ? pendingSnap.data().certifications || [] : [];

  await setDoc(doc(db, "users", cred.user.uid), {
    name,
    email,
    role: "aluno",
    purchasedCertifications,
    createdAt: serverTimestamp(),
  });

  if (pendingSnap.exists()) {
    await deleteDoc(pendingRef);
  }

  return cred.user;
}

export function login(email, password) {
  return signInWithEmailAndPassword(auth, email, password);
}

export function logout() {
  return signOut(auth);
}

onAuthStateChanged(auth, async (user) => {
  state.user = user;
  if (user) {
    const snap = await getDoc(doc(db, "users", user.uid));
    state.profile = snap.exists() ? snap.data() : { name: user.displayName, email: user.email, role: "aluno" };
    if (state.profile?.role === "aluno") {
      await checkDevice(user.uid);
    }
  } else {
    state.profile = null;
    state.deviceWarning = false;
  }
  state.ready = true;
  notify();
});

export function isAdmin() {
  return state.profile?.role === "admin";
}
