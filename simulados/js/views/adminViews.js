import {
  listCertifications,
  createCertification,
  deleteCertification,
  listQuestions,
  getQuestionsByIds,
  createQuestion,
  updateQuestion,
  deleteQuestion,
  listExams,
  getExam,
  createExam,
  updateExam,
  deleteExam,
  listAllAttempts,
  listStudents,
  grantAccess,
  revokeAccess,
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
      <p class="text-sm text-slate-500 mb-4">O acesso de um aluno a uma certificação é liberado automaticamente pela compra na Hotmart (ver README) ou manualmente na página <a href="#/admin/alunos" class="text-indigo-600 font-medium">Alunos</a>.</p>
      <form id="new-cert" class="flex gap-2 mb-6">
        <input name="name" required placeholder="Ex: CPA-20, CPA-10, CEA..." class="flex-1 border border-slate-300 rounded-lg px-3 py-2" />
        <input name="checkoutUrl" placeholder="Link de compra na Hotmart (opcional)" class="flex-1 border border-slate-300 rounded-lg px-3 py-2" />
        <button class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 rounded-lg">Adicionar</button>
      </form>
      <div class="bg-white rounded-xl shadow divide-y">
        ${
          certs
            .map(
              (c) => `
          <div class="p-4 flex items-center justify-between">
            <div>
              <span class="font-medium text-slate-800">${escapeHtml(c.name)}</span>
              ${c.checkoutUrl ? `<a href="${escapeHtml(c.checkoutUrl)}" target="_blank" class="block text-xs text-indigo-600">${escapeHtml(c.checkoutUrl)}</a>` : `<span class="block text-xs text-slate-400">Sem link de compra cadastrado</span>`}
            </div>
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
    await createCertification(fd.get("name"), fd.get("checkoutUrl"));
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
const TYPE_LABEL = { simples: "Simples", mae: "Estudo de caso", arvore: "Árvore de decisão" };
const TYPE_BADGE = { simples: "bg-slate-100 text-slate-600", mae: "bg-violet-50 text-violet-600", arvore: "bg-amber-50 text-amber-700" };

export async function renderAdminQuestoes(root) {
  root.innerHTML = `<div class="max-w-4xl mx-auto py-8">${adminNav("admin/questoes")}<p class="text-slate-500">Carregando...</p></div>`;
  const certs = await listCertifications();
  const filterId = root.dataset.certFilter || certs[0]?.id || "";
  // "filha" nunca aparece solta na lista: só existe pendurada em uma "mae".
  const questions = filterId ? (await listQuestions(filterId)).filter((q) => q.type !== "filha") : [];

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
                <div class="flex gap-2 mb-1">
                  <span class="inline-block text-xs font-semibold px-2 py-0.5 rounded ${TYPE_BADGE[q.type || "simples"]}">${TYPE_LABEL[q.type || "simples"]}</span>
                  ${q.module ? `<span class="inline-block text-xs font-semibold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded">${escapeHtml(q.module)}</span>` : ""}
                  ${q.type === "mae" ? `<span class="text-xs text-slate-400">${(q.childIds || []).length} pergunta(s)</span>` : ""}
                  ${q.type === "arvore" ? `<span class="text-xs text-slate-400">${(q.steps || []).length} interação(ões)</span>` : ""}
                </div>
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
    btn.addEventListener("click", async () => {
      const q = questions.find((x) => x.id === btn.dataset.id);
      await showQuestionForm(root.querySelector("#q-form-slot"), filterId, q, () => renderAdminQuestoes(root));
    })
  );
  root.querySelectorAll(".del-q").forEach((btn) =>
    btn.addEventListener("click", async () => {
      if (!confirm("Excluir esta questão? (se for um estudo de caso, as perguntas filhas também serão excluídas)")) return;
      const q = questions.find((x) => x.id === btn.dataset.id);
      if (q?.type === "mae") {
        for (const childId of q.childIds || []) await deleteQuestion(childId);
      }
      await deleteQuestion(btn.dataset.id);
      renderAdminQuestoes(root);
    })
  );
}

/* ---- Bloco de alternativas reutilizável (questão simples / cada filha / cada passo da árvore) ---- */
function optionsBlockHtml(prefix, options, correctIndex) {
  const opts = options?.length ? options : ["", ""];
  return `
    <div class="opts-wrap space-y-2" data-prefix="${prefix}">
      ${opts
        .map(
          (o, i) => `
        <div class="flex items-center gap-2 opt-row">
          <input type="radio" name="${prefix}-correctIndex" ${correctIndex === i ? "checked" : ""} required />
          <input type="text" name="${prefix}-opt" value="${escapeHtml(o)}" required placeholder="Alternativa ${i + 1}" class="flex-1 border border-slate-300 rounded-lg px-3 py-2 text-sm" />
          <button type="button" class="remove-opt text-red-400 text-xs px-1">✕</button>
        </div>
      `
        )
        .join("")}
    </div>
    <button type="button" class="add-opt text-indigo-600 text-xs font-semibold mt-2" data-prefix="${prefix}">+ Adicionar alternativa</button>
  `;
}

function videoFieldsHtml(prefix, question) {
  return `
    <div class="grid grid-cols-2 gap-3">
      <div>
        <label class="block text-xs font-medium text-slate-500 mb-1">Vídeo-explicação (URL, opcional)</label>
        <input name="${prefix}-videoUrl" value="${escapeHtml(question?.videoUrl || "")}" placeholder="https://youtube.com/..." class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
      </div>
      <div>
        <label class="block text-xs font-medium text-slate-500 mb-1">Professor (opcional)</label>
        <input name="${prefix}-videoProfessor" value="${escapeHtml(question?.videoProfessor || "")}" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
      </div>
    </div>
  `;
}

function childCardHtml(index, child) {
  return `
    <div class="border border-violet-200 rounded-lg p-4 mb-3 child-card" data-index="${index}">
      <input type="hidden" name="child-${index}-id" value="${child?.id || ""}" />
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-bold text-violet-600 uppercase tracking-wide">Pergunta filha ${index + 1}</span>
        <button type="button" class="remove-child text-red-500 text-xs font-semibold">Remover</button>
      </div>
      <div class="space-y-3">
        <textarea name="child-${index}-statement" required rows="2" placeholder="Pergunta referente ao caso acima..." class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(child?.statement || "")}</textarea>
        ${optionsBlockHtml(`child-${index}`, child?.options, child?.correctIndex)}
        <textarea name="child-${index}-explanation" rows="2" placeholder="Explicação do gabarito (opcional)" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(child?.explanation || "")}</textarea>
        ${videoFieldsHtml(`child-${index}`, child)}
      </div>
    </div>
  `;
}

function stepCardHtml(index, step) {
  return `
    <div class="border border-amber-200 rounded-lg p-4 mb-3 step-card" data-index="${index}">
      <div class="flex items-center justify-between mb-2">
        <span class="text-xs font-bold text-amber-700 uppercase tracking-wide">Interação ${index + 1}</span>
        <button type="button" class="remove-step text-red-500 text-xs font-semibold">Remover</button>
      </div>
      <div class="space-y-3">
        <textarea name="step-${index}-statement" required rows="2" placeholder="O que acontece nesta etapa / pergunta ao aluno..." class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(step?.statement || "")}</textarea>
        ${optionsBlockHtml(`step-${index}`, step?.options, step?.correctIndex)}
      </div>
    </div>
  `;
}

function typeFieldsHtml(type, question, children) {
  if (type === "mae") {
    const kids = children || [];
    return `
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-1">Contexto / situação do caso</label>
        <textarea name="statement" required rows="3" placeholder="Ex: Paula, 35 anos, é empresária do setor de tecnologia..." class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.statement || "")}</textarea>
      </div>
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-2">Perguntas sobre este caso</label>
        <div id="children-wrap" data-count="${kids.length}">
          ${kids.map((c, i) => childCardHtml(i, c)).join("")}
        </div>
        <button type="button" id="add-child" class="text-violet-600 text-xs font-semibold">+ Adicionar pergunta filha</button>
      </div>
    `;
  }
  if (type === "arvore") {
    const steps = question?.steps || [];
    return `
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-1">Situação inicial</label>
        <textarea name="statement" required rows="3" placeholder="Descreva o cenário que dá início às interações..." class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.statement || "")}</textarea>
      </div>
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-2">Interações em sequência</label>
        <div id="steps-wrap" data-count="${steps.length}">
          ${steps.map((s, i) => stepCardHtml(i, s)).join("")}
        </div>
        <button type="button" id="add-step" class="text-amber-700 text-xs font-semibold">+ Adicionar interação</button>
      </div>
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-1">Acertos necessários para considerar aprovado neste item</label>
        <input type="number" min="1" name="requiredCorrect" value="${question?.requiredCorrect ?? steps.length ?? 1}" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
      </div>
      <div>
        <label class="block text-sm font-medium text-slate-700 mb-1">Explicação geral (opcional)</label>
        <textarea name="explanation" rows="2" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.explanation || "")}</textarea>
      </div>
      ${videoFieldsHtml("root", question)}
    `;
  }
  // simples
  return `
    <div>
      <label class="block text-sm font-medium text-slate-700 mb-1">Enunciado</label>
      <textarea name="statement" required rows="3" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.statement || "")}</textarea>
    </div>
    <div>
      <label class="block text-sm font-medium text-slate-700 mb-1">Alternativas (marque a correta)</label>
      ${optionsBlockHtml("root", question?.options, question?.correctIndex)}
    </div>
    <div>
      <label class="block text-sm font-medium text-slate-700 mb-1">Explicação do gabarito (opcional)</label>
      <textarea name="explanation" rows="2" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm">${escapeHtml(question?.explanation || "")}</textarea>
    </div>
    ${videoFieldsHtml("root", question)}
  `;
}

async function showQuestionForm(slot, certificationId, question, onSaved) {
  const type = question?.type || "simples";
  let children = [];
  if (type === "mae" && question?.childIds?.length) {
    children = await getQuestionsByIds(question.childIds);
    children.sort((a, b) => (question.childIds.indexOf(a.id) - question.childIds.indexOf(b.id)));
  }

  slot.innerHTML = `
    <div class="bg-white rounded-xl shadow p-5 mb-6 border-2 border-indigo-100">
      <h3 class="font-semibold text-slate-800 mb-4">${question ? "Editar questão" : "Nova questão"}</h3>
      <form id="q-form" class="space-y-4">
        <div class="flex gap-4">
          <label class="text-sm flex items-center gap-1.5"><input type="radio" name="type" value="simples" ${type === "simples" ? "checked" : ""} /> Simples</label>
          <label class="text-sm flex items-center gap-1.5"><input type="radio" name="type" value="mae" ${type === "mae" ? "checked" : ""} /> Estudo de caso (mãe/filha)</label>
          <label class="text-sm flex items-center gap-1.5"><input type="radio" name="type" value="arvore" ${type === "arvore" ? "checked" : ""} /> Árvore de decisão</label>
        </div>
        <div>
          <label class="block text-sm font-medium text-slate-700 mb-1">Módulo / Tema (opcional)</label>
          <input name="module" value="${escapeHtml(question?.module || "")}" placeholder="Ex: Fundos de Investimento" class="w-full border border-slate-300 rounded-lg px-3 py-2 text-sm" />
        </div>
        <div id="type-fields">${typeFieldsHtml(type, question, children)}</div>
        <div class="flex gap-3">
          <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-5 py-2 rounded-lg text-sm">Salvar</button>
          <button type="button" id="cancel-q" class="text-slate-500 text-sm font-medium">Cancelar</button>
        </div>
      </form>
    </div>
  `;

  const form = slot.querySelector("#q-form");

  form.querySelectorAll('input[name="type"]').forEach((radio) => {
    radio.addEventListener("change", () => {
      slot.querySelector("#type-fields").innerHTML = typeFieldsHtml(radio.value, null, []);
    });
  });

  // Delegação de eventos para tudo que é dinâmico (alternativas, filhas, interações)
  form.addEventListener("click", (e) => {
    if (e.target.matches(".add-opt")) {
      const prefix = e.target.dataset.prefix;
      const wrap = form.querySelector(`.opts-wrap[data-prefix="${prefix}"]`);
      const div = document.createElement("div");
      div.className = "flex items-center gap-2 opt-row";
      div.innerHTML = `
        <input type="radio" name="${prefix}-correctIndex" required />
        <input type="text" name="${prefix}-opt" required placeholder="Nova alternativa" class="flex-1 border border-slate-300 rounded-lg px-3 py-2 text-sm" />
        <button type="button" class="remove-opt text-red-400 text-xs px-1">✕</button>
      `;
      wrap.appendChild(div);
    }
    if (e.target.matches(".remove-opt")) {
      const row = e.target.closest(".opt-row");
      if (row.parentElement.querySelectorAll(".opt-row").length > 2) row.remove();
      else alert("A questão precisa de pelo menos 2 alternativas.");
    }
    if (e.target.matches("#add-child")) {
      const wrap = form.querySelector("#children-wrap");
      const idx = Number(wrap.dataset.count || 0);
      wrap.insertAdjacentHTML("beforeend", childCardHtml(idx, null));
      wrap.dataset.count = idx + 1;
    }
    if (e.target.matches(".remove-child")) {
      e.target.closest(".child-card").remove();
    }
    if (e.target.matches("#add-step")) {
      const wrap = form.querySelector("#steps-wrap");
      const idx = Number(wrap.dataset.count || 0);
      wrap.insertAdjacentHTML("beforeend", stepCardHtml(idx, null));
      wrap.dataset.count = idx + 1;
    }
    if (e.target.matches(".remove-step")) {
      e.target.closest(".step-card").remove();
    }
  });

  slot.querySelector("#cancel-q").addEventListener("click", () => (slot.innerHTML = ""));

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const selectedType = form.querySelector('input[name="type"]:checked').value;
    const fd = new FormData(form);
    const module = fd.get("module") || "";

    if (selectedType === "mae") {
      const oldChildIds = new Set(question?.childIds || []);
      const childCards = Array.from(form.querySelectorAll(".child-card"));
      const newChildIds = [];
      for (const card of childCards) {
        const idx = card.dataset.index;
        const existingId = card.querySelector(`[name="child-${idx}-id"]`).value || null;
        const { options, correctIndex } = extractOptions(card, `child-${idx}`);
        const childData = {
          certificationId,
          type: "filha",
          module,
          statement: card.querySelector(`[name="child-${idx}-statement"]`).value,
          options,
          correctIndex,
          explanation: card.querySelector(`[name="child-${idx}-explanation"]`).value || "",
          videoUrl: card.querySelector(`[name="child-${idx}-videoUrl"]`).value || "",
          videoProfessor: card.querySelector(`[name="child-${idx}-videoProfessor"]`).value || "",
        };
        if (existingId) {
          await updateQuestion(existingId, childData);
          newChildIds.push(existingId);
          oldChildIds.delete(existingId);
        } else {
          const ref = await createQuestion(childData);
          newChildIds.push(ref.id);
        }
      }
      // Filhas que foram removidas no formulário: excluir do banco também.
      for (const removedId of oldChildIds) await deleteQuestion(removedId);

      const maeData = {
        certificationId,
        type: "mae",
        module,
        statement: form.querySelector('[name="statement"]').value,
        childIds: newChildIds,
      };
      if (question) await updateQuestion(question.id, maeData);
      else await createQuestion(maeData);
    } else if (selectedType === "arvore") {
      const steps = Array.from(form.querySelectorAll(".step-card")).map((card) => {
        const idx = card.dataset.index;
        const { options, correctIndex } = extractOptions(card, `step-${idx}`);
        return { statement: card.querySelector(`[name="step-${idx}-statement"]`).value, options, correctIndex };
      });
      const data = {
        certificationId,
        type: "arvore",
        module,
        statement: fd.get("statement"),
        steps,
        requiredCorrect: Number(fd.get("requiredCorrect") || steps.length || 1),
        explanation: fd.get("explanation") || "",
        videoUrl: fd.get("root-videoUrl") || "",
        videoProfessor: fd.get("root-videoProfessor") || "",
      };
      if (question) await updateQuestion(question.id, data);
      else await createQuestion(data);
    } else {
      const { options, correctIndex } = extractOptions(form, "root");
      const data = {
        certificationId,
        type: "simples",
        module,
        statement: fd.get("statement"),
        options,
        correctIndex,
        explanation: fd.get("explanation") || "",
        videoUrl: fd.get("root-videoUrl") || "",
        videoProfessor: fd.get("root-videoProfessor") || "",
      };
      if (question) await updateQuestion(question.id, data);
      else await createQuestion(data);
    }

    slot.innerHTML = "";
    onSaved();
  });
}

// Lê um bloco de alternativas (opts-wrap[data-prefix]) dentro de `scopeEl` e retorna { options, correctIndex }.
function extractOptions(scopeEl, prefix) {
  const wrap = scopeEl.querySelector(`.opts-wrap[data-prefix="${prefix}"]`);
  const optionInputs = Array.from(wrap.querySelectorAll(`input[name="${prefix}-opt"]`));
  const radios = Array.from(wrap.querySelectorAll(`input[name="${prefix}-correctIndex"]`));
  const options = optionInputs.map((el) => el.value);
  const checkedRadio = radios.find((r) => r.checked);
  const correctIndex = checkedRadio ? radios.indexOf(checkedRadio) : 0;
  return { options, correctIndex };
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
  const questions = (await listQuestions(certificationId)).filter((q) => q.type !== "filha");
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
                <span>
                  <span class="inline-block text-[10px] font-semibold px-1.5 py-0.5 rounded mr-1 ${TYPE_BADGE[q.type || "simples"]}">${TYPE_LABEL[q.type || "simples"]}</span>
                  ${escapeHtml(q.statement)}
                  ${q.type === "mae" ? `<span class="text-slate-400"> (${(q.childIds || []).length} perguntas)</span>` : ""}
                </span>
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
  const [attempts, students, certs] = await Promise.all([listAllAttempts(), listStudents(), listCertifications()]);

  const byUser = {};
  students.forEach((s) => {
    byUser[s.id] = {
      id: s.id,
      name: s.name || s.email,
      deviceSwitchCount: s.deviceSwitchCount || 0,
      purchasedCertifications: s.purchasedCertifications || [],
      attempts: [],
    };
  });
  attempts.forEach((a) => {
    (byUser[a.userId] ||= { id: a.userId, name: a.userName, deviceSwitchCount: 0, purchasedCertifications: [], attempts: [] }).attempts.push(a);
  });

  root.innerHTML = `
    <div class="max-w-4xl mx-auto py-8">
      ${adminNav("admin/alunos")}
      <h1 class="text-2xl font-bold text-slate-800 mb-6">Alunos e acesso</h1>
      <div class="space-y-4">
        ${
          Object.values(byUser)
            .map((u) => {
              const avg = u.attempts.length ? Math.round(u.attempts.reduce((s, a) => s + a.scorePercent, 0) / u.attempts.length) : null;
              return `
            <div class="bg-white rounded-xl shadow p-4">
              <div class="flex items-center justify-between mb-2">
                <p class="font-semibold text-slate-800">${escapeHtml(u.name)} ${u.deviceSwitchCount > 1 ? `<span class="text-xs font-medium text-amber-600 bg-amber-50 px-2 py-0.5 rounded align-middle">${u.deviceSwitchCount} trocas de dispositivo</span>` : ""}</p>
                ${avg !== null ? `<p class="text-sm font-bold ${avg >= 70 ? "text-emerald-600" : "text-red-600"}">Média: ${avg}%</p>` : `<p class="text-xs text-slate-400">Sem tentativas ainda</p>`}
              </div>
              <div class="text-xs text-slate-500 space-y-1 mb-3">
                ${u.attempts
                  .slice(0, 5)
                  .map((a) => `<div>${escapeHtml(a.examTitle)} — ${a.scorePercent}% — ${formatDate(a.finishedAt)}</div>`)
                  .join("")}
              </div>
              <div class="border-t border-slate-100 pt-3">
                <p class="text-xs font-semibold text-slate-500 mb-2">Acesso liberado:</p>
                <div class="flex flex-wrap gap-3">
                  ${certs
                    .map(
                      (c) => `
                    <label class="flex items-center gap-1.5 text-xs text-slate-700">
                      <input type="checkbox" class="access-toggle" data-user="${u.id}" data-cert="${c.id}" ${u.purchasedCertifications.includes(c.id) ? "checked" : ""} />
                      ${escapeHtml(c.name)}
                    </label>
                  `
                    )
                    .join("") || `<span class="text-xs text-slate-400">Cadastre uma certificação primeiro.</span>`}
                </div>
              </div>
            </div>
          `;
            })
            .join("") || `<p class="text-slate-500">Nenhum aluno cadastrado ainda.</p>`
        }
      </div>
    </div>
  `;

  root.querySelectorAll(".access-toggle").forEach((cb) => {
    cb.addEventListener("change", async () => {
      cb.disabled = true;
      if (cb.checked) await grantAccess(cb.dataset.user, cb.dataset.cert);
      else await revokeAccess(cb.dataset.user, cb.dataset.cert);
      cb.disabled = false;
    });
  });
}
