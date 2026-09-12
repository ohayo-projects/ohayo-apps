/* Runs before paint: enables JS-only styling and sends Russian-speaking first-time
   visitors to the ru page. Only the English pages redirect, so no loop is possible. */
(function () {
  var root = document.documentElement;
  root.classList.add("js");

  try {
    if (root.lang !== "en") return;
    if (localStorage.getItem("ohayo.lang")) return;
    if (!/^ru\b/i.test(navigator.language || "")) return;
    var alt = document.querySelector('link[rel="alternate"][hreflang="ru"]');
    // Same-origin hop by path: keeps preview deployments and local runs on their own host.
    if (alt && alt.href) location.replace(new URL(alt.href).pathname);
  } catch (e) { /* private mode, blocked storage — stay on the English page */ }
})();
