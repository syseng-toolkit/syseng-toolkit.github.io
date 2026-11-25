// Home page "Preview" links: open the template's live Sheet in a pop-up instead of a new tab.
// The link still works without JavaScript (it opens the Sheet in a new tab).
document.addEventListener("click", (e) => {
  const a = e.target.closest("a.sheet-peek");
  if (!a) return;
  e.preventDefault();

  const dlg = document.createElement("dialog");
  dlg.className = "sheet-peek-dialog";
  dlg.innerHTML = `
    <div class="sheet-peek-bar">
      <strong></strong>
      <a class="sheet-peek-page">Template page →</a>
      <span class="sheet-peek-note"></span>
      <button type="button" aria-label="Close" autofocus>✕</button>
    </div>
    <div class="sheet-peek-frame"><iframe></iframe></div>`;
  dlg.querySelector("strong").textContent = a.dataset.title + " template";
  const page = dlg.querySelector(".sheet-peek-page");
  if (a.dataset.page) page.href = a.dataset.page; else page.remove();
  const frame = dlg.querySelector("iframe");
  frame.title = a.dataset.title + " template, preview";
  frame.src = a.href;

  const close = () => dlg.close();
  dlg.querySelector("button").addEventListener("click", close);
  dlg.addEventListener("click", (ev) => { if (ev.target === dlg) close(); });  // click outside
  dlg.addEventListener("close", () => dlg.remove());

  document.body.appendChild(dlg);
  dlg.showModal();
});

// Home page gallery: arrows scroll one card at a time, and only show when the strip overflows.
document.querySelectorAll(".tpl-gallery").forEach((g) => {
  const track = g.querySelector(".tg-track");
  const step = () => (track.querySelector(".tg-card")?.offsetWidth || 300) + 16;
  g.querySelector(".tg-prev").addEventListener("click", () => track.scrollBy({ left: -step(), behavior: "smooth" }));
  g.querySelector(".tg-next").addEventListener("click", () => track.scrollBy({ left: step(), behavior: "smooth" }));
  const update = () => {
    const more = track.scrollWidth > track.clientWidth + 1;
    g.classList.toggle("tg-scrolls", more);
    g.querySelector(".tg-prev").disabled = track.scrollLeft < 8;
    g.querySelector(".tg-next").disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 8;
  };
  track.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  window.addEventListener("load", update);
  update();
});
