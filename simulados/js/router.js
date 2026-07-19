const routes = {};
let notFoundHandler = () => {};

export function registerRoute(pattern, handler) {
  // pattern ex: "aluno/simulado/:id" -> regex com grupos nomeados
  const paramNames = [];
  const regexStr = pattern
    .split("/")
    .map((seg) => {
      if (seg.startsWith(":")) {
        paramNames.push(seg.slice(1));
        return "([^/]+)";
      }
      return seg;
    })
    .join("/");
  routes[pattern] = { regex: new RegExp(`^${regexStr}$`), paramNames, handler };
}

export function setNotFound(handler) {
  notFoundHandler = handler;
}

export function navigate(path) {
  window.location.hash = "#/" + path.replace(/^#?\/?/, "");
}

function currentPath() {
  return window.location.hash.replace(/^#\/?/, "") || "";
}

export async function resolve() {
  const path = currentPath();
  for (const key in routes) {
    const { regex, paramNames, handler } = routes[key];
    const match = path.match(regex);
    if (match) {
      const params = {};
      paramNames.forEach((name, i) => (params[name] = decodeURIComponent(match[i + 1])));
      await handler(params);
      return;
    }
  }
  await notFoundHandler();
}

export function startRouter() {
  window.addEventListener("hashchange", resolve);
  resolve();
}
