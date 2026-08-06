const data = window.COOKBOOK_STYLES || { styles: [], categories: [], styleCount: 0 };

const state = {
  query: "",
  category: "All",
};

const searchInput = document.querySelector("#searchInput");
const categoryStrip = document.querySelector("#categoryStrip");
const featuredGrid = document.querySelector("#featuredGrid");
const styleGrid = document.querySelector("#styleGrid");
const resultCount = document.querySelector("#resultCount");
const activeFilter = document.querySelector("#activeFilter");
const emptyState = document.querySelector("#emptyState");
const detailPanel = document.querySelector("#detailPanel");
const detailContent = document.querySelector("#detailContent");
const toast = document.querySelector("#toast");
const pullSwitch = document.querySelector("#themePullSwitch");
let isPullAnimating = false;

function setTheme(theme) {
  const nextTheme = theme === "light" ? "light" : "dark";
  document.documentElement.dataset.theme = nextTheme;
  try {
    localStorage.setItem("cookbook-theme", nextTheme);
  } catch {
    // The theme still updates for this page load if storage is unavailable.
  }
  if (pullSwitch) {
    const targetTheme = nextTheme === "light" ? "dark" : "light";
    pullSwitch.setAttribute("aria-pressed", String(nextTheme === "light"));
    pullSwitch.setAttribute("aria-label", `Pull to switch to ${targetTheme} theme`);
    pullSwitch.title = `Pull to switch to ${targetTheme} theme`;
  }
}

function toggleThemeWithPull() {
  if (isPullAnimating) return;
  isPullAnimating = true;
  const currentTheme = document.documentElement.dataset.theme === "light" ? "light" : "dark";
  const nextTheme = currentTheme === "light" ? "dark" : "light";
  if (pullSwitch) {
    pullSwitch.classList.add("lamp-pull--pulling");
    window.setTimeout(() => {
      setTheme(nextTheme);
    }, 150);
    window.setTimeout(() => {
      pullSwitch.classList.remove("lamp-pull--pulling");
      pullSwitch.style.removeProperty("--pull-scale");
      pullSwitch.style.removeProperty("--bead-offset");
      isPullAnimating = false;
    }, 400);
    return;
  }
  setTheme(nextTheme);
  isPullAnimating = false;
}

function setupPullSwitch() {
  if (!pullSwitch) return;
  let startY = 0;
  let pullDistance = 0;
  let isDragging = false;
  let suppressClick = false;
  let activePointerId = null;

  function beginPull(clientY) {
    if (isPullAnimating) return false;
    isDragging = true;
    suppressClick = false;
    pullDistance = 0;
    startY = clientY;
    return true;
  }

  function updatePull(clientY) {
    if (!isDragging) return;
    pullDistance = Math.max(0, Math.min(42, clientY - startY));
    if (pullDistance > 2) suppressClick = true;
    pullSwitch.style.setProperty("--pull-scale", String(1 + pullDistance / 80));
    pullSwitch.style.setProperty("--bead-offset", `${pullDistance}px`);
  }

  function finishPull() {
    if (!isDragging) return;
    isDragging = false;
    activePointerId = null;
    const shouldToggle = pullDistance >= 22;
    pullSwitch.style.removeProperty("--pull-scale");
    pullSwitch.style.removeProperty("--bead-offset");
    if (shouldToggle) toggleThemeWithPull();
  }

  pullSwitch.addEventListener("pointerdown", (event) => {
    if (!beginPull(event.clientY)) return;
    activePointerId = event.pointerId;
    pullSwitch.setPointerCapture(event.pointerId);
  });

  pullSwitch.addEventListener("pointermove", (event) => {
    if (activePointerId !== event.pointerId) return;
    updatePull(event.clientY);
  });

  pullSwitch.addEventListener("pointerup", finishPull);
  pullSwitch.addEventListener("pointercancel", finishPull);

  pullSwitch.addEventListener("mousedown", (event) => {
    if (activePointerId !== null || event.button !== 0) return;
    beginPull(event.clientY);
  });

  document.addEventListener("mousemove", (event) => {
    if (activePointerId !== null) return;
    updatePull(event.clientY);
  });

  document.addEventListener("mouseup", () => {
    if (activePointerId !== null) return;
    finishPull();
  });

  pullSwitch.addEventListener(
    "touchstart",
    (event) => {
      if (activePointerId !== null || event.touches.length === 0) return;
      beginPull(event.touches[0].clientY);
    },
    { passive: true },
  );

  pullSwitch.addEventListener(
    "touchmove",
    (event) => {
      if (activePointerId !== null || event.touches.length === 0) return;
      updatePull(event.touches[0].clientY);
    },
    { passive: true },
  );

  pullSwitch.addEventListener("touchend", () => {
    if (activePointerId !== null) return;
    finishPull();
  });

  pullSwitch.addEventListener("click", (event) => {
    event.stopPropagation();
    if (suppressClick) {
      suppressClick = false;
      return;
    }
    toggleThemeWithPull();
  });
}

function textIncludes(style, query) {
  if (!query) return true;
  const haystack = [
    style.name,
    style.slug,
    style.category,
    style.description,
    style.summary,
    style.anchors.join(" "),
    style.variables.join(" "),
  ]
    .join(" ")
    .toLowerCase();
  return haystack.includes(query.toLowerCase());
}

function visibleStyles() {
  return data.styles.filter((style) => {
    const categoryMatch = state.category === "All" || style.category === state.category;
    return categoryMatch && textIncludes(style, state.query.trim());
  });
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function cardTemplate(style, featured = false) {
  const cardClass = featured ? "style-card featured" : "style-card";
  return `
    <article class="${cardClass}" data-slug="${escapeHtml(style.slug)}">
      <button class="preview-button" type="button" data-open-detail="${escapeHtml(style.slug)}">
        <img src="${escapeHtml(style.preview16)}" alt="${escapeHtml(style.name)} preview" loading="lazy">
      </button>
      <div class="card-body">
        <span class="category-label">${escapeHtml(style.category)}</span>
        <h3>${escapeHtml(style.name)}</h3>
        <p class="card-description">${escapeHtml(style.description)}</p>
        <div class="card-actions">
          <button class="action-button primary" type="button" data-open-detail="${escapeHtml(style.slug)}">Details</button>
          <button class="action-button" type="button" data-copy-prompt="${escapeHtml(style.slug)}">Copy Prompt</button>
          <a class="card-link" href="${escapeHtml(style.styleJson)}">style.json</a>
          <a class="card-link" href="${escapeHtml(style.preview9)}">9:16</a>
        </div>
      </div>
    </article>
  `;
}

function renderCategories() {
  const categories = ["All", ...data.categories];
  categoryStrip.innerHTML = categories
    .map((category) => {
      const active = category === state.category ? " is-active" : "";
      return `<button class="category-button${active}" type="button" data-category="${escapeHtml(category)}">${escapeHtml(category)}</button>`;
    })
    .join("");
}

function renderFeatured() {
  featuredGrid.innerHTML = data.styles.slice(0, 6).map((style) => cardTemplate(style, true)).join("");
}

function renderGrid() {
  const styles = visibleStyles();
  styleGrid.innerHTML = styles.map((style) => cardTemplate(style)).join("");
  resultCount.textContent = `${styles.length} of ${data.styleCount} styles`;
  activeFilter.textContent = state.category === "All" ? "All categories" : state.category;
  emptyState.hidden = styles.length > 0;
}

function findStyle(slug) {
  return data.styles.find((style) => style.slug === slug);
}

function detailTemplate(style) {
  return `
    <div class="detail-content">
      <span class="category-label">${escapeHtml(style.category)}</span>
      <h2>${escapeHtml(style.name)}</h2>
      <p>${escapeHtml(style.summary || style.description)}</p>
      <div class="detail-images">
        <img src="${escapeHtml(style.preview16)}" alt="${escapeHtml(style.name)} 16:9 preview">
        <img src="${escapeHtml(style.preview9)}" alt="${escapeHtml(style.name)} 9:16 preview">
      </div>
      <h3>Style Anchors</h3>
      <ul class="anchor-list">
        ${style.anchors.map((anchor) => `<li>${escapeHtml(anchor)}</li>`).join("")}
      </ul>
      <h3>Variables</h3>
      <ul class="variable-list">
        ${style.variables.map((variable) => `<li>${escapeHtml(variable)}</li>`).join("")}
      </ul>
      <div class="detail-actions">
        <button class="action-button primary" type="button" data-copy-prompt="${escapeHtml(style.slug)}">Copy Prompt</button>
        <a class="card-link" href="${escapeHtml(style.styleJson)}">Open style.json</a>
        <a class="card-link" href="${escapeHtml(style.copyPromptDoc)}">Prompt doc</a>
        <a class="card-link" href="${escapeHtml(style.folder)}">Folder</a>
      </div>
    </div>
  `;
}

function openDetail(slug) {
  const style = findStyle(slug);
  if (!style) return;
  detailContent.innerHTML = detailTemplate(style);
  detailPanel.classList.add("is-open");
  detailPanel.setAttribute("aria-hidden", "false");
}

function closeDetail() {
  detailPanel.classList.remove("is-open");
  detailPanel.setAttribute("aria-hidden", "true");
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("is-visible");
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    toast.classList.remove("is-visible");
  }, 1800);
}

function fallbackCopy(text) {
  const area = document.createElement("textarea");
  area.value = text;
  area.setAttribute("readonly", "");
  area.style.position = "fixed";
  area.style.opacity = "0";
  document.body.append(area);
  area.select();
  document.execCommand("copy");
  area.remove();
}

async function copyPrompt(slug) {
  const style = findStyle(slug);
  if (!style) return;
  try {
    await navigator.clipboard.writeText(style.copyPrompt);
  } catch {
    fallbackCopy(style.copyPrompt);
  }
  showToast(`Copied ${style.name}`);
}

document.addEventListener("click", (event) => {
  const categoryButton = event.target.closest("[data-category]");
  if (categoryButton) {
    state.category = categoryButton.dataset.category;
    renderCategories();
    renderGrid();
    return;
  }

  const detailButton = event.target.closest("[data-open-detail]");
  if (detailButton) {
    openDetail(detailButton.dataset.openDetail);
    return;
  }

  const copyButton = event.target.closest("[data-copy-prompt]");
  if (copyButton) {
    copyPrompt(copyButton.dataset.copyPrompt);
    return;
  }

  if (event.target.closest("[data-close-detail]")) {
    closeDetail();
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") closeDetail();
});

searchInput.addEventListener("input", () => {
  state.query = searchInput.value;
  renderGrid();
});

setupPullSwitch();
setTheme(document.documentElement.dataset.theme);
renderCategories();
renderFeatured();
renderGrid();
