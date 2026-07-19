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
  serverTimestamp,
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

// Estado global simples do usuário logado + seu perfil (role: 'aluno' | 'admin')
export const state = {
  user: null,
  profile: null,
  ready: false,
};

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
  await setDoc(doc(db, "users", cred.user.uid), {
    name,
    email,
    role: "aluno",
    createdAt: serverTimestamp(),
  });
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
  } else {
    state.profile = null;
  }
  state.ready = true;
  notify();
});

export function isAdmin() {
  return state.profile?.role === "admin";
}
