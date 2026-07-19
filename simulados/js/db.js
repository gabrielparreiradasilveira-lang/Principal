import { db } from "./firebase-config.js";
import {
  collection,
  doc,
  addDoc,
  updateDoc,
  deleteDoc,
  getDoc,
  getDocs,
  query,
  where,
  orderBy,
  serverTimestamp,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

/* ---------------- Certificações ---------------- */
// Ex: { name: "CPA-20" }
export async function listCertifications() {
  const snap = await getDocs(query(collection(db, "certifications"), orderBy("name")));
  return snap.docs.map((d) => ({ id: d.id, ...d.data() }));
}

export async function createCertification(name) {
  return addDoc(collection(db, "certifications"), { name, createdAt: serverTimestamp() });
}

export async function deleteCertification(id) {
  return deleteDoc(doc(db, "certifications", id));
}

/* ---------------- Questões ---------------- */
// { certificationId, module, statement, options: [string,...], correctIndex, explanation, difficulty }
export async function listQuestions(certificationId) {
  let q = collection(db, "questions");
  if (certificationId) {
    q = query(q, where("certificationId", "==", certificationId));
  }
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() }));
}

export async function getQuestionsByIds(ids) {
  const results = [];
  for (const id of ids) {
    const snap = await getDoc(doc(db, "questions", id));
    if (snap.exists()) results.push({ id: snap.id, ...snap.data() });
  }
  return results;
}

export async function createQuestion(data) {
  return addDoc(collection(db, "questions"), { ...data, createdAt: serverTimestamp() });
}

export async function updateQuestion(id, data) {
  return updateDoc(doc(db, "questions", id), data);
}

export async function deleteQuestion(id) {
  return deleteDoc(doc(db, "questions", id));
}

/* ---------------- Simulados (exams) ---------------- */
// { certificationId, title, description, timeLimitMinutes, passScorePercent, questionIds: [], shuffleQuestions, published }
export async function listExams(certificationId, onlyPublished = false) {
  let q = collection(db, "exams");
  const clauses = [];
  if (certificationId) clauses.push(where("certificationId", "==", certificationId));
  if (onlyPublished) clauses.push(where("published", "==", true));
  if (clauses.length) q = query(q, ...clauses);
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() }));
}

export async function getExam(id) {
  const snap = await getDoc(doc(db, "exams", id));
  return snap.exists() ? { id: snap.id, ...snap.data() } : null;
}

export async function createExam(data) {
  return addDoc(collection(db, "exams"), { ...data, createdAt: serverTimestamp() });
}

export async function updateExam(id, data) {
  return updateDoc(doc(db, "exams", id), data);
}

export async function deleteExam(id) {
  return deleteDoc(doc(db, "exams", id));
}

/* ---------------- Tentativas (attempts) ---------------- */
// { userId, examId, certificationId, answers: {questionId: optionIndex}, correctCount, totalCount, scorePercent, passed, startedAt, finishedAt }
export async function createAttempt(data) {
  return addDoc(collection(db, "attempts"), { ...data, finishedAt: serverTimestamp() });
}

export async function listAttemptsByUser(userId) {
  const q = query(collection(db, "attempts"), where("userId", "==", userId));
  const snap = await getDocs(q);
  return snap.docs
    .map((d) => ({ id: d.id, ...d.data() }))
    .sort((a, b) => (b.finishedAt?.seconds ?? 0) - (a.finishedAt?.seconds ?? 0));
}

export async function listAllAttempts() {
  const snap = await getDocs(collection(db, "attempts"));
  return snap.docs
    .map((d) => ({ id: d.id, ...d.data() }))
    .sort((a, b) => (b.finishedAt?.seconds ?? 0) - (a.finishedAt?.seconds ?? 0));
}

export async function listStudents() {
  const q = query(collection(db, "users"), where("role", "==", "aluno"));
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() }));
}
