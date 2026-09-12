/* Progressive enhancement only: the page is complete without this file. */
(function () {
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("stuck", window.scrollY > 8); };
    onScroll();
    addEventListener("scroll", onScroll, { passive: true });
  }

  var hint = document.querySelector(".lang-hint");
  document.querySelectorAll("[data-lang]").forEach(function (el) {
    el.addEventListener("click", function () {
      try { localStorage.setItem("ohayo.lang", el.dataset.lang); } catch (e) {}
      if (hint) hint.hidden = true;
    });
  });

  // A suggestion, not a redirect: Google advises against locale redirects, and crawlers
  // and shared links must land on the page they asked for.
  if (hint) {
    try {
      if (!localStorage.getItem("ohayo.lang") && /^ru\b/i.test(navigator.language || "")) hint.hidden = false;
    } catch (e) { /* storage blocked: stay quiet */ }
  }

  var targets = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window) || matchMedia("(prefers-reduced-motion: reduce)").matches) {
    targets.forEach(function (el) { el.classList.add("in"); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry, i) {
      if (!entry.isIntersecting) return;
      setTimeout(function () { entry.target.classList.add("in"); }, Math.min(i, 6) * 60);
      io.unobserve(entry.target);
    });
  }, { rootMargin: "0px 0px -12% 0px", threshold: .12 });
  targets.forEach(function (el) { io.observe(el); });
})();
