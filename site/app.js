const state = {
  episodes: [],
  selected: null,
  query: "",
};

const episodeList = document.querySelector("#episodeList");
const summary = document.querySelector("#summary");
const search = document.querySelector("#search");
const title = document.querySelector("#episodeTitle");
const meta = document.querySelector("#episodeMeta");
const transcript = document.querySelector("#transcript");
const transcriptLink = document.querySelector("#transcriptLink");
const playerLink = document.querySelector("#playerLink");
const selectedCover = document.querySelector("#selectedCover");
const defaultCover = "https://images.podigee-cdn.net/0x,sL3rd-8gIENV0jDGxTRhEKOYzoUhn4Sgs9-d3rsTM_Hk=/https://main.podigee-cdn.net/uploads/u73317/3c6e6a97-b38f-40cb-8890-7ce7916cb31c.jpg";

function padEpisode(value) {
  return String(value).padStart(3, "0");
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function linkifyUrls(value) {
  return value.replace(/https?:\/\/[^\s<]+/g, (match) => {
    let url = match;
    let suffix = "";
    while (/[.,!?;:)\]]$/.test(url)) {
      suffix = `${url.slice(-1)}${suffix}`;
      url = url.slice(0, -1);
    }
    const href = url.replaceAll("&amp;", "&");
    return `<a href="${escapeHtml(href)}" target="_blank" rel="noreferrer">${url}</a>${suffix}`;
  });
}

function renderInlineMarkdown(value) {
  const withTimestamps = escapeHtml(value).replace(/\*\*\[(\d\d:\d\d:\d\d)\]\*\*/g, '<span class="timestamp">[$1]</span>');
  const withStrong = withTimestamps.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  return linkifyUrls(withStrong);
}

function renderMarkdown(markdown) {
  const lines = markdown.split(/\r?\n/);
  const body = [];
  let inFrontmatter = false;

  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (index === 0 && line.trim() === "---") {
      inFrontmatter = true;
      continue;
    }
    if (inFrontmatter) {
      if (line.trim() === "---") inFrontmatter = false;
      continue;
    }
    if (!line.trim()) continue;
    if (line.startsWith("# ")) {
      body.push(`<h1>${escapeHtml(line.slice(2))}</h1>`);
      continue;
    }
    if (line.startsWith("## ")) {
      body.push(`<h2>${escapeHtml(line.slice(3))}</h2>`);
      continue;
    }
    body.push(`<p>${renderInlineMarkdown(line)}</p>`);
  }

  return body.join("");
}

function filteredEpisodes() {
  const query = state.query.trim().toLowerCase();
  if (!query) return state.episodes;
  return state.episodes.filter((episode) => {
    return `${episode.index} ${episode.title}`.toLowerCase().includes(query);
  });
}

function renderList() {
  const episodes = filteredEpisodes();
  episodeList.innerHTML = "";

  for (const episode of episodes) {
    const imageUrl = episode.imageUrl || defaultCover;
    const button = document.createElement("button");
    button.type = "button";
    button.className = `episode-button${episode.transcriptAvailable ? "" : " missing"}${state.selected?.index === episode.index ? " active" : ""}`;
    button.innerHTML = `
      <img class="episode-cover" src="${escapeHtml(imageUrl)}" alt="">
      <span class="episode-number">${padEpisode(episode.index)}</span>
      <span>
        <span class="episode-title">${escapeHtml(episode.title)}</span>
        <span class="episode-status">${episode.transcriptAvailable ? "Transkript verfügbar" : "Noch kein Transkript"}</span>
      </span>
    `;
    button.addEventListener("click", () => selectEpisode(episode));
    episodeList.append(button);
  }
}

async function selectEpisode(episode) {
  state.selected = episode;
  renderList();

  title.textContent = episode.title;
  meta.textContent = `Folge ${padEpisode(episode.index)}${episode.duration ? ` · ${episode.duration}` : ""}`;
  playerLink.href = episode.pageUrl || "https://think-ai.podigee.io/";
  selectedCover.src = episode.imageUrl || defaultCover;
  selectedCover.alt = `Cover: ${episode.title}`;

  if (!episode.transcriptAvailable) {
    transcriptLink.href = episode.pageUrl || "#";
    transcriptLink.setAttribute("aria-disabled", "true");
    transcript.innerHTML = `<p class="empty-state">Für diese Folge liegt noch kein Markdown-Transkript vor. Der Webplayer ist bereits verfügbar.</p>`;
    return;
  }

  transcriptLink.removeAttribute("aria-disabled");
  transcriptLink.href = episode.transcriptPath;
  transcript.innerHTML = `<p class="empty-state">Lade Transkript...</p>`;

  try {
    const response = await fetch(episode.transcriptPath);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const markdown = await response.text();
    transcript.innerHTML = renderMarkdown(markdown);
  } catch (error) {
    transcript.innerHTML = `<p class="empty-state">Das Transkript konnte nicht geladen werden. Öffne die Markdown-Datei direkt über den Link oben.</p>`;
  }
}

async function init() {
  try {
    const response = await fetch("data/episodes.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const data = await response.json();
    state.episodes = data.episodes.slice().sort((a, b) => b.index - a.index);
    summary.textContent = `${data.availableTranscriptCount} von ${data.episodeCount} Transkripten verfügbar`;
    renderList();

    const firstAvailable = state.episodes.find((episode) => episode.transcriptAvailable) || state.episodes[0];
    if (firstAvailable) selectEpisode(firstAvailable);
  } catch (error) {
    summary.textContent = "Daten konnten nicht geladen werden";
    transcript.innerHTML = `<p class="empty-state">Die Episodendaten sind nicht verfügbar.</p>`;
  }
}

search.addEventListener("input", (event) => {
  state.query = event.target.value;
  renderList();
});

init();
