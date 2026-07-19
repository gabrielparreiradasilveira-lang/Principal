import {
  listCertifications,
  createCertification,
  deleteCertification,
  listQuestions,
  createQuestion,
  updateQuestion,
  deleteQuestion,
  listExams,
  getExam,
  createExam,
  updateExam,
  deleteExam,
  listAllAttempts,
} from "../db.js";
import { escapeHtml, formatDate } from "../utils.js";
import { navigate } from "../router.js";

function adminNav(active) {
  const items = [
    ["admin", "Visão geral"],
    ["admin/questoes", "Questões"],
    ["admin/simulados", "Simulados"],
    ["admin/certificacoes", "Certificações"],
    ["admin/alunos", "Alunos"],
  ];
  return `
    <div class="flex gap-2 mb-6 overflow-x-auto">
      ${items
        .map(
          ([path, label]) => `
        <a href="#/${path}" class="px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap ${active === path ? "bg-indigo-600 text-white" : "bg-white text-slate-600 border border-slate-200"}">${label}</a>
      `
        )
        .join("")}
    </div>
  `;
}

async function certOptions(selectedId) {
  const certs = await listCertifications();
  return certs
    .map((c) => `<option value="${c.id}" ${c.id === selectedId ? "selected" : ""}>${escapeHtml(c.name)}</option>`)
    .join("");
}

/* ---------------- Visão geral ---------------- */
export async function renderAdminHome(root) {
  root.innerHTML = `<div class="max-w-5xl mx-auto py-8">${adminNav("admin")}<p class="text-slate-500">Carregando...</p></div>`;
  const [certs, attempts] = await Promise.all([listCertifications(), listAllAttempts()]);
  let totalQuestions = 0;
  let totalExams = 0;
  for (const c of certs) {
    totalQuestions += (await listQuestions(c.id)).length;
    totalExams += (await listExams(c.id)).length;
  }

  root.innerHTML = `
    <div class="max-w-5xl mx-auto py-8">
      ${adminNav("admin")}
      <h1 class="text-2xl font-bold text-slate-800 mb-6">Painel administrativo</h1>
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-8">
        ${statCard("Certificações", certs.length)}
        ${statCard("Questões", totalQuestions)}
        ${statCard("Simulados", totalExams)}
        ${statCard("Tentativas", attempts.length)}
      </div>
      <h2 class="text-lg font-bold text-slate-800 mb-3">Últimas tentativas</h2>
      <div class="bg-white rounded-xl shadow divide-y">
        ${
          attempts.slice(0, 10).map(
            (a) => `
          <div class="p-4 flex items-center justify-between text-sm">
            <div>
              <p class="font-medium text-slate-800">${escapeHtml(a.userName || "Aluno")}</p>
              <p class="text-slate-500">${escapeHtml(a.examTitle)} · ${formatDate(a.finishedAt)}</p>
            </div>
            <span class="font-bold ${a.passed ? "text-emerald-600" : "text-red-600"}">${a.scorePercent}%</span>
          </div>
        `
          ).join("") || `<p class="p-4 text-slate-500">Nenhuma tentativa ainda.</p>`
        }
      </div>
    </div>
  `;
}

function statCard(label, value) {
  return `<div class="bg-white rounded-xl shadow p-4"><p class="text-2xl font-extrabold text-slate-800">${value}</p><p class="text-xs text-slate-500 mt-1">${label}</p></div>`;
}

/* ---------------- Certificações ---------------- */
export async function renderAdminCertificacoes(root) {
  root.innerHTML = `<div class="max-w-3xl mx-auto py-8">${adminNav("admin/certificacoes")}<p class="text-slate-500">Carregando...</p></div>`;
  const certs = await listCertifications();

  root.innerHTML = `
    <div class="max-w-3xl mx-auto py-8">
      ${adminNav("admin/certificacoes")}
      <h1 class="text-2xl font-bold text-slate-800 mb-6">Certificações</h1>
      <form id="new-cert" class="flex gap-2 mb-6">
        <input name="name" required placeholder="Ex: CPA-20, CPA-10, CEA..." class="flex-1 border border-slate-300 rounded-lg px-3 py-2" />
        <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 rounded-lg">Adicionar</button>
      </form>
      <div class="bg-white rounded-xl shadow divide-y">
        ${
          certs
            .map(
              (c) => `
          <div class="p-4 flex items-center justify-between">
            <span class="font-medium text-slate-800">${escapeHtml(c.name)}</span>
            <button data-id="${c.id}" class="del-cert text-red-600 text-sm font-medium">Excluir</button>
          </div>
        `
            )
            .join("") || `<p class="p-4 text-slate-500">Nenhuma certificação cadastrada.</p>`
        }
      </div>
    </div>
  `;

  root.querySelector("#new-cert").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(e.target);
    await createCertification(fd.get("name"));
    renderAdminCertificacoes(root);
  });
  root.querySelectorAll(".del-cert").forEach((btn) =>
    btn.addEventListener("click", async () => {
      if (!confirm("Excluir esta certificação? (questões e simulados vinculados não serão apagados automaticamente)")) return;
      await deleteCertification(btn.dataset.id);
      renderAdminCertificacoes(root);
    })
  );
}

/* ---------------- Questões ---------------- */
export async function renderAdminQuestoes(root) {
  root.innerHTML = `<div class="max-w-4xl mx-auto py-8">${adminNav("admin/questoes")}<p class="text-slate-500">Carregando...</p></div>`;
  const certs = await listCertifications();
  const filterId = root.dataset.certFilter || certs[0]?.id || "";
  const questions = filterId ? await listQuestions(filterId) : [];

  root.innerHTML = `
    <div class="max-w-4xl mx-auto py-8">
      ${adminNav("admin/questoes")}
      <div class="flex items-center justify-between mb-6">
        <h1 class="text-2xl font-bold text-slate-800">Questões</h1>
        <button id="new-q-btn" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-lg text-sm">+ Nova questão</button>
      </div>

      <div class="mb-4">
        <select id="cert-filter" class="border border-slate-300 rounded-lg px-3 py-2 text-sm">
          ${certs.map((c) => `<option value="${c.id}" ${c.id === filterId ? "selected" : ""}>${escapeHtml(c.name)}</option>`).join("")}
        </select>
      </div>

      <div id="q-form-slot"></div>

      <div class="space-y-3" id="q-list">
        ${
          questions
            .map(
              (q) => `
          <div class="bg-white rounded-xl shadow p-4">
            <div class="flex items-start justify-between gap-3">
              <div class="flex-1">
                ${q.module ? `<span class="inline-block text-xs font-semibold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded mb-1">${escapeHtml(q.module)}</span>` : ""}
                <p class="text-slate-800 text-sm">${escapeHtml(q.statement)}</p>
              </div>
              <div class="flex gap-2 shrink-0">
                <button data-id="${q.id}" class="edit-q text-indigo-600 text-xs font-semibold">Editar</button>
                <button data-id="${q.id}" class="del-q text-red-600 text-xs font-semibold">Excluir</button>
              </div>
            </div>
          </div>
        `
            )
            .join("") || `<p class="text-slate-500">Nenhuma questão cadastrada para esta certificação.</p>`
        }
      </div>
    </div>
  `;

  root.querySelector("#cert-filter").addEventListener("change", (e) => {
    root.dataset.certFilter = e.target.value;
    renderAdminQuestoes(root);
  });

  root.querySelector("#new-q-btn").addEventListener("click", () => {
    showQuestionForm(root.querySelector("#q-form-slot"), filterId, null, () => renderAdminQuestoes(root));
  });

  root.querySelectorAll(".edit-q").forEach((btn) =>
    btn.addEventListener("click", () => {
      const q = questions.find((x) => x.id === btn.dataset.id);
      showQuestionForm(root.querySelector("#q-form-slot"), filterId, q, () => renderAdminQuestoes(root));
    })
  );
  root.querySelectorAll(".del-q").forEach((btn) =>
    btn.addEventListener("click", async () => {
      if (!confirm("Excluir esta questão?")) return;
      await deleteQuestion(btn.dataset.id);
      renderAdminQuestoes(root);
    })
  );
}

function showQuestionForm(slot, certificationId, question, onSaved) {
  const opts = question?.options || ["", "", "", ""];
  slot.innerHTML = `
    <div class="bg-white rounded-xl shadow p-5 mb-6 border-2 border-indigo-100">
      <h3 class="font-semibold text-slate-800 mb-4">${question ? "Editar questão" : "Nova questão"}</h3>
      <form id="q-form" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Módulo / Tema (opcional)</label>
          <input name="module" value="${escapeHtml(question?.module || "")}" placeholder="Ex: Fundos de Investimento" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Enunciado</label>
          <textarea name="statement" required rows="3" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.statement || "")}</textarea>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Alternativas (marque a correta)</label>
          <div id="opts-wrap" class="space-y-2">
            ${opts
              .map(
                (o, i) => `
              <div class="flex items-center gap-2">
                <input type="radio" name="correctIndex" value="${i}" ${question?.correctIndex === i ? "checked" : ""} required />
                <input type="text" name="opt-${i}" value="${escapeHtml(o)}" required placeholder="Alternativa ${i + 1}" class="flex-1 border border-slate-300 rounded-lg px-3 py-2 text-sm" />
              </div>
            `
              )
              .join("")}
          </div>
          <div class="flex gap-3 mt-2">
            <button type="button" id="add-opt" class="text-indigo-600 text-xs font-semibold">+ Adicionar alternativa</button>
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Explicação do gabarito (opcional)</label>
          <textarea name="explanation" rows="2" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.explanation || "")}</textarea>
        </div>
        <div class="flex gap-3">
          <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-5 py-2 rounded-lg text-sm">Salvar</button>
          <button type="button" id="cancel-q" class="text-slate-500 text-sm font-medium">Cancelar</button>
        </div>
      </form>
    </div>
  `;

  let optCount = opts.length;
  slot.querySelector("#add-opt").addEventListener("click", () => {
    const wrap = slot.querySelector("#opts-wrap");
    const div = document.createElement("div");
    div.className = "flex items-center gap-2";
    div.innerHTML = `
      <input type="radio" name="correctIndex" value="${optCount}" required />
      <input type="text" name="opt-${optCount}" required placeholder="Alternativa ${optCount + 1}" class="flex-1 border border-slate-300 rounded-lg px-3 py-2 text-sm" />
    `;
    wrap.appendChild(div);
    optCount++;
  });

  slot.querySelector("#cancel-q").addEventListener("click", () => (slot.innerHTML = ""));

  slot.querySelector("#q-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(e.target);
    const options = [];
    let i = 0;
    while (fd.has(`opt-${i}`)) {
      options.push(fd.get(`opt-${i}`));
      i++;
    }
    const data = {
      certificationId,
      module: fd.get("module") || "",
      statement: fd.get("statement"),
      options,
      correctIndex: Number(fd.get("correctIndex")),
      explanation: fd.get("explanation") || "",
    };
    if (question) {
      await updateQuestion(question.id, data);
    } else {
      await createQuestion(data);
    }
    slot.innerHTML = "";
    onSaved();
  });
}

/* ---------------- Simulados ---------------- */
export async function renderAdminSimulados(root) {
  root.innerHTML = `<div class="max-w-4xl mx-auto py-8">${adminNav("admin/simulados")}<p class="text-slate-500">Carregando...</p></div>`;
  const certs = await listCertifications();
  const filterId = root.dataset.certFilter || certs[0]?.id || "";
  const exams = filterId ? await listExams(filterId) : [];

  root.innerHTML = `
    <div class="max-w-4xl mx-auto py-8">
      ${adminNav("admin/simulados")}
      <div class="flex items-center justify-between mb-6">
        <h1 class="text-2xl font-bold text-slate-800">Simulados</h1>
        <button id="new-exam-btn" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-lg text-sm">+ Novo simulado</button>
      </div>
      <div class="mb-4">
        <select id="cert-filter" class="border border-slate-300 rounded-lg px-3 py-2 text-sm">
          ${certs.map((c) => `<option value="${c.id}" ${c.id === filterId ? "selected" : ""}>${escapeHtml(c.name)}</option>`).join("")}
        </select>
      </div>
      <div id="exam-form-slot"></div>
      <div class="space-y-3">
        ${
          exams
            .map(
              (ex) => `
          <div class="bg-white rounded-xl shadow p-4 flex items-center justify-between">
            <div>
              <p class="font-semibold text-slate-800">${escapeHtml(ex.title)} ${ex.published ? '<span class="text-xs text-emerald-600 font-semibold">(publicado)</span>' : '<span class="text-xs text-amber-600 font-semibold">(rascunho)</span>'}</p>
              <p class="text-xs text-slate-500 mt-1">${(ex.questionIds || []).length} questões · ${ex.timeLimitMinutes || 0} min · aprovação ${ex.passScorePercent || 70}%</p>
            </div>
            <div class="flex gap-2">
              <button data-id="${ex.id}" class="edit-exam text-indigo-600 text-xs font-semibold">Editar</button>
              <button data-id="${ex.id}" class="del-exam text-red-600 text-xs font-semibold">Excluir</button>
            </div>
          </div>
        `
            )
            .join("") || `<p class="text-slate-500">Nenhum simulado cadastrado para esta certificação.</p>`
        }
      </div>
    </div>
  `;

  root.querySelector("#cert-filter").addEventListener("change", (e) => {
    root.dataset.certFilter = e.target.value;
    renderAdminSimulados(root);
  });
  root.querySelector("#new-exam-btn").addEventListener("click", async () => {
    await showExamForm(root.querySelector("#exam-form-slot"), filterId, null, () => renderAdminSimulados(root));
  });
  root.querySelectorAll(".edit-exam").forEach((btn) =>
    btn.addEventListener("click", async () => {
      const exam = await getExam(btn.dataset.id);
      await showExamForm(root.querySelector("#exam-form-slot"), filterId, exam, () => renderAdminSimulados(root));
    })
  );
  root.querySelectorAll(".del-exam").forEach((btn) =>
    btn.addEventListener("click", async () => {
      if (!confirm("Excluir este simulado?")) return;
      await deleteExam(btn.dataset.id);
      renderAdminSimulados(root);
    })
  );
}

async function showExamForm(slot, certificationId, exam, onSaved) {
  const questions = await listQuestions(certificationId);
  const selectedIds = new Set(exam?.questionIds || []);

  slot.innerHTML = `
    <div class="bg-white rounded-xl shadow p-5 mb-6 border-2 border-indigo-100">
      <h3 class="font-semibold text-slate-800 mb-4">${exam ? "Editar simulado" : "Novo simulado"}</h3>
      <form id="exam-form" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Título</label>
          <input name="title" required value="${escapeHtml(exam?.title || "")}" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Descrição (opcional)</label>
          <input name="description" value="${escapeHtml(exam?.description || "")}" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Tempo limite (min, 0 = sem limite)</label>
            <input type="number" min="0" name="timeLimitMinutes" value="${exam?.timeLimitMinutes ?? 60}" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
          </div>
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Nota de aprovação (%)</label>
            <input type="number" min="0" max="100" name="passScorePercent" value="${exam?.passScorePercent ?? 70}" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
          </div>
        </div>
        <label class="flex items-center gap-2 text-sm text-slate-700">
          <input type="checkbox" name="shuffleQuestions" ${exam?.shuffleQuestions ? "checked" : ""} /> Embaralhar ordem das questões
        </label>
        <label class="flex items-center gap-2 text-sm text-slate-700">
          <input type="checkbox" name="published" ${exam?.published ? "checked" : ""} /> Publicado (visível para alunos)
        </label>

        <div>
          <label class="block text-sm font-medium text-slate-700 mb-2">Selecionar questões (${questions.length} disponíveis nesta certificação)</label>
          <div class="max-h-64 overflow-y-auto border border-slate-200 rounded-lg divide-y">
            ${
              questions
                .map(
                  (q) => `
              <label class="flex items-start gap-2 p-3 text-sm cursor-pointer hover:bg-slate-50">
                <input type="checkbox" name="qid" value="${q.id}" ${selectedIds.has(q.id) ? "checked" : ""} class="mt-1" />
                <span>${escapeHtml(q.statement)}</span>
              </label>
            `
                )
                .join("") || `<p class="p-3 text-slate-500">Cadastre questões nesta certificação primeiro.</p>`
            }
          </div>
        </div>

        <div class="flex gap-3">
          <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-5 py-2 rounded-lg text-sm">Salvar</button>
          <button type="button" id="cancel-exam" class="text-slate-500 text-sm font-medium">Cancelar</button>
        </div>
      </form>
    </div>
  `;

  slot.querySelector("#cancel-exam").addEventListener("click", () => (slot.innerHTML = ""));

  slot.querySelector("#exam-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(e.target);
    const data = {
      certificationId,
      title: fd.get("title"),
      description: fd.get("description") || "",
      timeLimitMinutes: Number(fd.get("timeLimitMinutes") || 0),
      passScorePercent: Number(fd.get("passScorePercent") || 70),
      shuffleQuestions: fd.get("shuffleQuestions") === "on",
      published: fd.get("published") === "on",
      questionIds: fd.getAll("qid"),
    };
    if (exam) {
      await updateExam(exam.id, data);
    } else {
      await createExam(data);
    }
    slot.innerHTML = "";
    onSaved();
  });
}

/* ---------------- Alunos ---------------- */
export async function renderAdminAlunos(root) {
  root.innerHTML = `<div class="max-w-4xl mx-auto py-8">${adminNav("admin/alunos")}<p class="text-slate-500">Carregando...</p></div>`;
  const attempts = await listAllAttempts();

  const byUser = {};
  attempts.forEach((a) => {
    const key = a.userId;
    (byUser[key] ||= { name: a.userName, attempts: [] }).attempts.push(a);
  });

  root.innerHTML = `
    <div class="max-w-4xl mx-auto py-8">
      ${adminNav("admin/alunos")}
      <h1 class="text-2xl font-bold text-slate-800 mb-6">Desempenho dos alunos</h1>
      <div class="space-y-4">
        ${
          Object.values(byUser)
            .map((u) => {
              const avg = Math.round(u.attempts.reduce((s, a) => s + a.scorePercent, 0) / u.attempts.length);
              return `
            <div class="bg-white rounded-xl shadow p-4">
              <div class="flex items-center justify-between mb-2">
                <p class="font-semibold text-slate-800">${escapeHtml(u.name)}</p>
                <p class="text-sm font-bold ${avg >= 70 ? "text-emerald-600" : "text-red-600"}">Média: ${avg}%</p>
              </div>
              <div class="text-xs text-slate-500 space-y-1">
                ${u.attempts
                  .slice(0, 5)
                  .map((a) => `<div>${escapeHtml(a.examTitle)} — ${a.scorePercent}% — ${formatDate(a.finishedAt)}</div>`)
                  .join("")}
              </div>
            </div>
          `;
            })
            .join("") || `<p class="text-slate-500">Nenhuma tentativa registrada ainda.</p>`
        }
      </div>
    </div>
  `;
}
