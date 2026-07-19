import { state } from "../auth.js";
import {
  listCertifications,
  listExams,
  getExam,
  getQuestionsByIds,
  createAttempt,
  listAttemptsByUser,
} from "../db.js";
import { shuffle, formatTime, formatDate, escapeHtml } from "../utils.js";
import { navigate } from "../router.js";

export async function renderAlunoDashboard(root) {
  root.innerHTML = `<div class="max-w-4xl mx-auto py-8"><p class="text-slate-500">Carregando simulados...</p></div>`;

  const [certifications, allExams] = await Promise.all([listCertifications(), listAllPublishedExams()]);

  const examsByCert = {};
  allExams.forEach((exam) => {
    (examsByCert[exam.certificationId] ||= []).push(exam);
  });

  const sections = certifications
    .filter((c) => (examsByCert[c.id] || []).length > 0)
    .map(
      (c) => `
      <div class="mb-8">
        <h2 class="text-lg font-bold text-slate-800 mb-3">${escapeHtml(c.name)}</h2>
        <div class="grid gap-4 sm:grid-cols-2">
          ${examsByCert[c.id]
            .map(
              (exam) => `
            <div class="bg-white rounded-xl shadow p-5 flex flex-col justify-between">
              <div>
                <h3 class="font-semibold text-slate-800">${escapeHtml(exam.title)}</h3>
                <p class="text-sm text-slate-500 mt-1">${escapeHtml(exam.description || "")}</p>
                <div class="flex gap-3 mt-3 text-xs text-slate-500">
                  <span>📝 ${(exam.questionIds || []).length} questões</span>
                  <span>⏱ ${exam.timeLimitMinutes || 0} min</span>
                  <span>✅ Aprovação: ${exam.passScorePercent || 70}%</span>
                </div>
              </div>
              <button data-exam="${exam.id}" class="start-exam mt-4 bg-indigo-600 hover:bg-indigo-700 text-white text-sm font-semibold py-2 rounded-lg transition">Iniciar simulado</button>
            </div>
          `
            )
            .join("")}
        </div>
      </div>
    `
    )
    .join("");

  root.innerHTML = `
    <div class="max-w-4xl mx-auto py-8">
      <div class="flex items-center justify-between mb-6">
        <h1 class="text-2xl font-bold text-slate-800">Simulados disponíveis</h1>
        <a href="#/aluno/historico" class="text-indigo-600 text-sm font-medium">Ver meu histórico →</a>
      </div>
      ${sections || `<p class="text-slate-500">Nenhum simulado publicado ainda. Volte em breve.</p>`}
    </div>
  `;

  root.querySelectorAll(".start-exam").forEach((btn) => {
    btn.addEventListener("click", () => navigate(`aluno/simulado/${btn.dataset.exam}`));
  });
}

async function listAllPublishedExams() {
  const certs = await listCertifications();
  const results = [];
  for (const c of certs) {
    const exams = await listExams(c.id, true);
    results.push(...exams);
  }
  return results;
}

export async function renderSimuladoRunner(root, examId) {
  root.innerHTML = `<div class="max-w-3xl mx-auto py-8"><p class="text-slate-500">Carregando simulado...</p></div>`;

  const exam = await getExam(examId);
  if (!exam) {
    root.innerHTML = `<div class="max-w-3xl mx-auto py-8"><p class="text-red-600">Simulado não encontrado.</p></div>`;
    return;
  }
  let questions = await getQuestionsByIds(exam.questionIds || []);
  if (exam.shuffleQuestions) questions = shuffle(questions);

  const runner = {
    examId: exam.id,
    startedAt: Date.now(),
    current: 0,
    answers: {}, // questionId -> optionIndex
    secondsLeft: (exam.timeLimitMinutes || 0) * 60,
    timer: null,
  };

  function renderQuestion() {
    const q = questions[runner.current];
    const total = questions.length;
    const answered = Object.keys(runner.answers).length;

    root.innerHTML = `
      <div class="max-w-3xl mx-auto py-8">
        <div class="flex items-center justify-between mb-4">
          <div>
            <h1 class="text-lg font-bold text-slate-800">${escapeHtml(exam.title)}</h1>
            <p class="text-sm text-slate-500">Questão ${runner.current + 1} de ${total} · ${answered} respondidas</p>
          </div>
          ${
            exam.timeLimitMinutes
              ? `<div id="timer" class="text-lg font-mono font-bold ${runner.secondsLeft < 60 ? "text-red-600" : "text-slate-700"}">${formatTime(runner.secondsLeft)}</div>`
              : ""
          }
        </div>

        <div class="w-full bg-slate-200 rounded-full h-2 mb-6">
          <div class="bg-indigo-600 h-2 rounded-full transition-all" style="width:${((runner.current + 1) / total) * 100}%"></div>
        </div>

        <div class="bg-white rounded-2xl shadow p-6">
          ${q.module ? `<span class="inline-block text-xs font-semibold text-indigo-600 bg-indigo-50 px-2 py-1 rounded mb-3">${escapeHtml(q.module)}</span>` : ""}
          <p class="text-slate-800 font-medium mb-5 whitespace-pre-wrap">${escapeHtml(q.statement)}</p>
          <div class="space-y-2" id="options">
            ${(q.options || [])
              .map(
                (opt, i) => `
              <label class="flex items-start gap-3 border rounded-lg p-3 cursor-pointer transition ${runner.answers[q.id] === i ? "border-indigo-600 bg-indigo-50" : "border-slate-200 hover:border-indigo-300"}">
                <input type="radio" name="option" value="${i}" class="mt-1" ${runner.answers[q.id] === i ? "checked" : ""} />
                <span class="text-slate-700 text-sm">${escapeHtml(opt)}</span>
              </label>
            `
              )
              .join("")}
          </div>
        </div>

        <div class="flex items-center justify-between mt-6">
          <button id="prev-btn" class="px-4 py-2 rounded-lg border border-slate-300 text-slate-600 font-medium disabled:opacity-40" ${runner.current === 0 ? "disabled" : ""}>Anterior</button>
          <div class="flex gap-2">
            ${
              runner.current < total - 1
                ? `<button id="next-btn" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white font-semibold">Próxima</button>`
                : `<button id="finish-btn" class="px-5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-semibold">Finalizar simulado</button>`
            }
          </div>
        </div>
      </div>
    `;

    root.querySelectorAll('input[name="option"]').forEach((input) => {
      input.addEventListener("change", (e) => {
        runner.answers[q.id] = Number(e.target.value);
        renderQuestion();
      });
    });
    root.querySelector("#prev-btn")?.addEventListener("click", () => {
      runner.current = Math.max(0, runner.current - 1);
      renderQuestion();
    });
    root.querySelector("#next-btn")?.addEventListener("click", () => {
      runner.current = Math.min(total - 1, runner.current + 1);
      renderQuestion();
    });
    root.querySelector("#finish-btn")?.addEventListener("click", () => finish(false));
  }

  async function finish(timeUp) {
    if (runner.timer) clearInterval(runner.timer);
    let correctCount = 0;
    questions.forEach((q) => {
      if (runner.answers[q.id] === q.correctIndex) correctCount++;
    });
    const total = questions.length;
    const scorePercent = total ? Math.round((correctCount / total) * 100) : 0;
    const passed = scorePercent >= (exam.passScorePercent || 70);

    const attemptRef = await createAttempt({
      userId: state.user.uid,
      userName: state.profile?.name || state.user.email,
      examId: exam.id,
      examTitle: exam.title,
      certificationId: exam.certificationId,
      answers: runner.answers,
      correctCount,
      totalCount: total,
      scorePercent,
      passed,
      timeUp: !!timeUp,
      durationSeconds: Math.round((Date.now() - runner.startedAt) / 1000),
    });

    navigate(`aluno/resultado/${attemptRef.id}`);
  }

  if (exam.timeLimitMinutes) {
    runner.timer = setInterval(() => {
      runner.secondsLeft--;
      const timerEl = document.getElementById("timer");
      if (timerEl) {
        timerEl.textContent = formatTime(runner.secondsLeft);
        if (runner.secondsLeft < 60) timerEl.classList.add("text-red-600");
      }
      if (runner.secondsLeft <= 0) {
        clearInterval(runner.timer);
        finish(true);
      }
    }, 1000);
  }

  renderQuestion();
}

export async function renderResultado(root, attemptId) {
  root.innerHTML = `<div class="max-w-3xl mx-auto py-8"><p class="text-slate-500">Carregando resultado...</p></div>`;

  const attempts = await listAttemptsByUser(state.user.uid);
  const attempt = attempts.find((a) => a.id === attemptId);
  if (!attempt) {
    root.innerHTML = `<div class="max-w-3xl mx-auto py-8"><p class="text-red-600">Resultado não encontrado.</p></div>`;
    return;
  }
  const exam = await getExam(attempt.examId);
  const questions = await getQuestionsByIds(exam?.questionIds || []);

  root.innerHTML = `
    <div class="max-w-3xl mx-auto py-8">
      <div class="bg-white rounded-2xl shadow p-6 mb-6 text-center">
        <p class="text-sm text-slate-500 mb-1">${escapeHtml(attempt.examTitle)}</p>
        <p class="text-5xl font-extrabold ${attempt.passed ? "text-emerald-600" : "text-red-600"}">${attempt.scorePercent}%</p>
        <p class="mt-2 font-semibold ${attempt.passed ? "text-emerald-600" : "text-red-600"}">${attempt.passed ? "Aprovado ✅" : "Reprovado ❌"}</p>
        <p class="text-sm text-slate-500 mt-1">${attempt.correctCount} de ${attempt.totalCount} questões corretas</p>
        ${attempt.timeUp ? `<p class="text-xs text-amber-600 mt-1">Tempo esgotado</p>` : ""}
      </div>

      <h2 class="text-lg font-bold text-slate-800 mb-3">Revisão das questões</h2>
      <div class="space-y-4">
        ${questions
          .map((q, idx) => {
            const chosen = attempt.answers[q.id];
            const correct = q.correctIndex;
            const isCorrect = chosen === correct;
            return `
            <div class="bg-white rounded-xl shadow p-5">
              <p class="text-sm font-semibold ${isCorrect ? "text-emerald-600" : "text-red-600"} mb-2">${isCorrect ? "✔ Correta" : "✘ Incorreta"} · Questão ${idx + 1}</p>
              <p class="text-slate-800 mb-3 whitespace-pre-wrap">${escapeHtml(q.statement)}</p>
              <div class="space-y-1 mb-3">
                ${(q.options || [])
                  .map((opt, i) => {
                    let cls = "border-slate-200";
                    if (i === correct) cls = "border-emerald-500 bg-emerald-50";
                    else if (i === chosen) cls = "border-red-500 bg-red-50";
                    return `<div class="border rounded-lg px-3 py-2 text-sm ${cls}">${escapeHtml(opt)} ${i === correct ? "<span class='text-emerald-600 font-semibold'>(gabarito)</span>" : ""} ${i === chosen && i !== correct ? "<span class='text-red-600 font-semibold'>(sua resposta)</span>" : ""}</div>`;
                  })
                  .join("")}
              </div>
              ${q.explanation ? `<p class="text-sm text-slate-600 bg-slate-50 rounded-lg p-3"><span class="font-semibold">Explicação: </span>${escapeHtml(q.explanation)}</p>` : ""}
            </div>
          `;
          })
          .join("")}
      </div>

      <div class="mt-6 flex gap-3">
        <a href="#/aluno" class="px-5 py-2 rounded-lg border border-slate-300 text-slate-600 font-medium">Voltar aos simulados</a>
        <a href="#/aluno/historico" class="px-5 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white font-semibold">Ver histórico</a>
      </div>
    </div>
  `;
}

export async function renderHistorico(root) {
  root.innerHTML = `<div class="max-w-3xl mx-auto py-8"><p class="text-slate-500">Carregando histórico...</p></div>`;
  const attempts = await listAttemptsByUser(state.user.uid);

  root.innerHTML = `
    <div class="max-w-3xl mx-auto py-8">
      <h1 class="text-2xl font-bold text-slate-800 mb-6">Meu histórico</h1>
      ${
        attempts.length === 0
          ? `<p class="text-slate-500">Você ainda não realizou nenhum simulado.</p>`
          : `<div class="space-y-3">
        ${attempts
          .map(
            (a) => `
          <a href="#/aluno/resultado/${a.id}" class="block bg-white rounded-xl shadow p-4 hover:shadow-md transition">
            <div class="flex items-center justify-between">
              <div>
                <p class="font-semibold text-slate-800">${escapeHtml(a.examTitle)}</p>
                <p class="text-xs text-slate-500 mt-1">${formatDate(a.finishedAt)}</p>
              </div>
              <div class="text-right">
                <p class="text-xl font-bold ${a.passed ? "text-emerald-600" : "text-red-600"}">${a.scorePercent}%</p>
                <p class="text-xs ${a.passed ? "text-emerald-600" : "text-red-600"}">${a.passed ? "Aprovado" : "Reprovado"}</p>
              </div>
            </div>
          </a>
        `
          )
          .join("")}
      </div>`
      }
    </div>
  `;
}
