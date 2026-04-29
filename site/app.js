const state = {
  episodes: [],
  selected: null,
  query: "",
  language: "de",
};

const episodeList = document.querySelector("#episodeList");
const summary = document.querySelector("#summary");
const search = document.querySelector("#search");
const title = document.querySelector("#episodeTitle");
const meta = document.querySelector("#episodeMeta");
const transcript = document.querySelector("#transcript");
const transcriptLink = document.querySelector("#transcriptLink");
const playerLink = document.querySelector("#playerLink");
const podcastPlayer = document.querySelector("#podcastPlayer");
const selectedCover = document.querySelector("#selectedCover");
const languageSwitch = document.querySelector(".language-switch");
const languageButtons = Array.from(document.querySelectorAll("[data-language]"));
const feedbackForm = document.querySelector("#feedbackForm");
const feedbackTitle = document.querySelector("#feedbackTitle");
const feedbackMessage = document.querySelector("#feedbackMessage");
const defaultCover = "https://images.podigee-cdn.net/0x,sL3rd-8gIENV0jDGxTRhEKOYzoUhn4Sgs9-d3rsTM_Hk=/https://main.podigee-cdn.net/uploads/u73317/3c6e6a97-b38f-40cb-8890-7ce7916cb31c.jpg";
const feedbackRecipient = "charta.ei.4z@icloud.com";
const podigeePlayerScript = "https://player.podigee-cdn.net/podcast-player/javascripts/podigee-podcast-player.js";

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

function submitFeedback(event) {
  event.preventDefault();
  if (!feedbackForm.reportValidity()) return;

  const body = [
    "Titel:",
    feedbackTitle.value.trim(),
    "",
    "Nachricht:",
    feedbackMessage.value.trim(),
  ].join("\n");
  const mailto = `mailto:${feedbackRecipient}?subject=${encodeURIComponent("PODCAST FEEDBACK")}&body=${encodeURIComponent(body)}`;
  window.location.href = mailto;
}

function playerEmbedUrl(episode) {
  if (episode.embedUrl) return episode.embedUrl;
  if (!episode.pageUrl) return "";
  return `${episode.pageUrl.replace(/\/$/, "")}/embed?context=external`;
}

function renderPodcastPlayer(episode) {
  podcastPlayer.replaceChildren();
  if (state.language !== "de") {
    podcastPlayer.hidden = true;
    return;
  }

  const embedUrl = playerEmbedUrl(episode);
  podcastPlayer.hidden = !embedUrl;
  if (!embedUrl) return;

  const script = document.createElement("script");
  script.className = "podigee-podcast-player";
  script.src = podigeePlayerScript;
  script.setAttribute("data-configuration", embedUrl);
  podcastPlayer.append(script);
}

function transcriptFor(episode, language = state.language) {
  if (episode.transcripts?.[language]) return episode.transcripts[language];
  if (language === "en") {
    return {
      available: Boolean(episode.englishTranscriptAvailable),
      path: episode.englishTranscriptPath || "",
    };
  }
  return {
    available: Boolean(episode.transcriptAvailable),
    path: episode.transcriptPath || "",
  };
}

function hasEnglishTranscript(episode) {
  return Boolean(episode && transcriptFor(episode, "en").available);
}

function updateLanguageSwitch(episode = state.selected) {
  if (languageSwitch) {
    languageSwitch.hidden = !hasEnglishTranscript(episode);
  }

  for (const button of languageButtons) {
    const language = button.dataset.language;
    button.classList.toggle("active", language === state.language);
    button.setAttribute("aria-pressed", String(language === state.language));
  }
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
    const selectedTranscript = transcriptFor(episode);
    const statusText = state.language === "en"
      ? (selectedTranscript.available ? "English transcript" : "English pending")
      : (selectedTranscript.available ? "Transkript verfügbar" : "Noch kein Transkript");
    const imageUrl = episode.imageUrl || defaultCover;
    const button = document.createElement("button");
    button.type = "button";
    button.className = `episode-button${selectedTranscript.available ? "" : " missing"}${state.selected?.index === episode.index ? " active" : ""}`;
    button.innerHTML = `
      <img class="episode-cover" src="${escapeHtml(imageUrl)}" alt="">
      <span class="episode-number">${padEpisode(episode.index)}</span>
      <span>
        <span class="episode-title">${escapeHtml(episode.title)}</span>
        <span class="episode-status">${statusText}</span>
      </span>
    `;
    button.addEventListener("click", () => selectEpisode(episode));
    episodeList.append(button);
  }
}

async function selectEpisode(episode) {
  state.selected = episode;
  if (state.language === "en" && !hasEnglishTranscript(episode)) {
    state.language = "de";
  }
  updateLanguageSwitch(episode);
  renderList();

  title.textContent = episode.title;
  meta.textContent = `Folge ${padEpisode(episode.index)}${episode.duration ? ` · ${episode.duration}` : ""}`;
  playerLink.href = episode.pageUrl || "https://think-ai.podigee.io/";
  playerLink.hidden = state.language !== "de";
  selectedCover.src = episode.imageUrl || defaultCover;
  selectedCover.alt = `Cover: ${episode.title}`;
  renderPodcastPlayer(episode);

  const selectedTranscript = transcriptFor(episode);
  if (!selectedTranscript.available) {
    transcriptLink.href = episode.pageUrl || "#";
    transcriptLink.setAttribute("aria-disabled", "true");
    transcript.innerHTML = state.language === "en"
      ? `<p class="empty-state">English translation is not available for this episode yet. The German transcript is available.</p>`
      : `<p class="empty-state">Für diese Folge liegt noch kein Markdown-Transkript vor. Der Webplayer ist bereits verfügbar.</p>`;
    return;
  }

  transcriptLink.removeAttribute("aria-disabled");
  transcriptLink.href = selectedTranscript.path;
  transcript.innerHTML = `<p class="empty-state">Lade Transkript...</p>`;

  try {
    const response = await fetch(selectedTranscript.path);
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
    summary.textContent = `${data.availableTranscriptCount} Deutsch · ${data.availableEnglishTranscriptCount || 0} English · ${data.episodeCount} Folgen`;
    updateLanguageSwitch();
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

for (const button of languageButtons) {
  button.addEventListener("click", () => {
    state.language = button.dataset.language;
    updateLanguageSwitch();
    if (state.selected) selectEpisode(state.selected);
  });
}

feedbackForm.addEventListener("submit", submitFeedback);

init();
