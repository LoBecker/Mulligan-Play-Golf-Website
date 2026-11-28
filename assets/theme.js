/* Hell und Dunkel. Ohne Wahl folgt die Seite dem Gerät (prefers-color-scheme).
   Der Knopf neben DE/EN merkt sich die Wahl in diesem Browser (localStorage "theme": "light" oder "dark").
   Läuft im <head>, bevor die Seite gezeichnet wird, damit nichts aufblitzt. Ohne JavaScript bleibt der Knopf
   ausgeblendet und die Seite folgt dem Gerät. */
(function () {
  var root = document.documentElement;
  var key = "theme";
  var saved = null;
  try { saved = localStorage.getItem(key); } catch (e) { /* Speicher gesperrt: dann wie das Gerät */ }
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  root.classList.add("js");

  var system = window.matchMedia("(prefers-color-scheme: light)");
  function current() {
    var chosen = root.getAttribute("data-theme");
    if (chosen === "light" || chosen === "dark") return chosen;
    return system.matches ? "light" : "dark";
  }
  function label(button) {
    // Der Knopf nennt, wohin er schaltet
    var next = current() === "light" ? "dark" : "light";
    button.setAttribute("aria-label", button.getAttribute("data-label-" + next));
    var color = getComputedStyle(root).getPropertyValue("--theme-color").trim();
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta && color) meta.setAttribute("content", color);
  }

  document.addEventListener("DOMContentLoaded", function () {
    var button = document.querySelector(".theme");
    if (!button) return;
    label(button);
    button.addEventListener("click", function () {
      var next = current() === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem(key, next); } catch (e) { /* nur für diese Seite */ }
      label(button);
    });
    if (system.addEventListener) system.addEventListener("change", function () { label(button); });
  });
})();
