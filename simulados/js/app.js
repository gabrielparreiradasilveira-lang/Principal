import { state, onStateChange, logout, isAdmin } from "./auth.js";
import { registerRoute, setNotFound, startRouter, navigate } from "./router.js";
import { renderLogin, renderSignup } from "./views/authViews.js";
import { renderAlunoDashboard, renderSimuladoRunner, renderResultado, renderHistorico } from "./views/alunoViews.js";
import {
  renderAdminHome,
  renderAdminQuestoes,
  renderAdminSimulados,
  renderAdminCertificacoes,
  renderAdminAlunos,
} from "./views/adminViews.js";

const app = document.getElementById("app");
const navBar = document.getElementById("navbar");

function renderNav() {
  if (!state.user) {
    navBar.innerHTML = `
      <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
        <span class="font-extrabold text-indigo-600">Simulados TopInvest</span>
        <div class="flex gap-4 text-sm font-medium">
          <a href="#/login" class="text-slate-600">Entrar</a>
          <a href="#/cadastro" class="text-indigo-600">Cadastrar</a>
        </div>
      </div>`;
    return;
  }
  const links = isAdmin()
    ? `<a href="#/admin" class="text-slate-600">Admin</a>`
    : `<a href="#/aluno" class="text-slate-600">Simulados</a><a href="#/aluno/historico" class="text-slate-600">Histórico</a>`;
  navBar.innerHTML = `
    <div class="max-w-5xl mx-auto px-4 py-3 flex items-center justify-between">
      <span class="font-extrabold text-indigo-600">Simulados TopInvest</span>
      <div class="flex items-center gap-4 text-sm font-medium">
        ${links}
        <span class="text-slate-400">${state.profile?.name || state.user.email}</span>
        <button id="logout-btn" class="text-red-600">Sair</button>
      </div>
    </div>`;
  document.getElementById("logout-btn")?.addEventListener("click", async () => {
    await logout();
    navigate("login");
  });
}

function requireAuth(handler) {
  return async (params) => {
    if (!state.user) return navigate("login");
    return handler(app, params.id ?? params);
  };
}

function requireAdmin(handler) {
  return async (params) => {
    if (!state.user) return navigate("login");
    if (!isAdmin()) return navigate("aluno");
    return handler(app, params.id ?? params);
  };
}

registerRoute("login", async () => {
  if (state.user) return navigate(isAdmin() ? "admin" : "aluno");
  renderLogin(app);
});
registerRoute("cadastro", async () => {
  if (state.user) return navigate(isAdmin() ? "admin" : "aluno");
  renderSignup(app);
});

registerRoute("aluno", requireAuth((root) => renderAlunoDashboard(root)));
registerRoute("aluno/historico", requireAuth((root) => renderHistorico(root)));
registerRoute("aluno/simulado/:id", requireAuth((root, params) => renderSimuladoRunner(root, params.id)));
registerRoute("aluno/resultado/:id", requireAuth((root, params) => renderResultado(root, params.id)));

registerRoute("admin", requireAdmin((root) => renderAdminHome(root)));
registerRoute("admin/questoes", requireAdmin((root) => renderAdminQuestoes(root)));
registerRoute("admin/simulados", requireAdmin((root) => renderAdminSimulados(root)));
registerRoute("admin/certificacoes", requireAdmin((root) => renderAdminCertificacoes(root)));
registerRoute("admin/alunos", requireAdmin((root) => renderAdminAlunos(root)));

setNotFound(async () => {
  if (!state.user) return navigate("login");
  return navigate(isAdmin() ? "admin" : "aluno");
});

let started = false;
onStateChange(() => {
  renderNav();
  if (!started) {
    started = true;
    startRouter(); // first call after auth state is known, avoids redirect flicker
  } else {
    import("./router.js").then(({ resolve }) => resolve());
  }
});
