import { signup, login } from "../auth.js";
import { navigate } from "../router.js";

export function renderLogin(root) {
  root.innerHTML = `
    <div class="max-w-md mx-auto mt-16 bg-white rounded-2xl shadow p-8">
      <h1 class="text-2xl font-bold text-slate-800 mb-1">Entrar</h1>
      <p class="text-slate-500 mb-6 text-sm">Acesse para fazer seus simulados.</p>
      <form id="login-form" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">E-mail</label>
          <input type="email" name="email" required class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Senha</label>
          <input type="password" name="password" required class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>
        <p id="login-error" class="text-sm text-red-600 hidden"></p>
        <button type="submit" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2.5 rounded-lg transition">Entrar</button>
      </form>
      <p class="text-sm text-slate-500 mt-4 text-center">
        Não tem conta? <a href="#/cadastro" class="text-indigo-600 font-medium">Cadastre-se</a>
      </p>
    </div>
  `;

  root.querySelector("#login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const errEl = root.querySelector("#login-error");
    errEl.classList.add("hidden");
    const fd = new FormData(e.target);
    try {
      await login(fd.get("email"), fd.get("password"));
      navigate("aluno");
    } catch (err) {
      errEl.textContent = friendlyError(err);
      errEl.classList.remove("hidden");
    }
  });
}

export function renderSignup(root) {
  root.innerHTML = `
    <div class="max-w-md mx-auto mt-16 bg-white rounded-2xl shadow p-8">
      <h1 class="text-2xl font-bold text-slate-800 mb-1">Criar conta</h1>
      <p class="text-slate-500 mb-6 text-sm">Cadastre-se para começar a praticar.</p>
      <form id="signup-form" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Nome completo</label>
          <input type="text" name="name" required class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">E-mail</label>
          <input type="email" name="email" required class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Senha</label>
          <input type="password" name="password" minlength="6" required class="w-full border border-slate-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500" />
        </div>
        <p id="signup-error" class="text-sm text-red-600 hidden"></p>
        <button type="submit" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2.5 rounded-lg transition">Criar conta</button>
      </form>
      <p class="text-sm text-slate-500 mt-4 text-center">
        Já tem conta? <a href="#/login" class="text-indigo-600 font-medium">Entrar</a>
      </p>
    </div>
  `;

  root.querySelector("#signup-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const errEl = root.querySelector("#signup-error");
    errEl.classList.add("hidden");
    const fd = new FormData(e.target);
    try {
      await signup(fd.get("name"), fd.get("email"), fd.get("password"));
      navigate("aluno");
    } catch (err) {
      errEl.textContent = friendlyError(err);
      errEl.classList.remove("hidden");
    }
  });
}

function friendlyError(err) {
  const code = err?.code || "";
  const map = {
    "auth/email-already-in-use": "Este e-mail já está cadastrado.",
    "auth/invalid-email": "E-mail inválido.",
    "auth/weak-password": "A senha precisa ter pelo menos 6 caracteres.",
    "auth/invalid-credential": "E-mail ou senha incorretos.",
    "auth/user-not-found": "E-mail ou senha incorretos.",
    "auth/wrong-password": "E-mail ou senha incorretos.",
  };
  return map[code] || "Ocorreu um erro. Tente novamente.";
}
