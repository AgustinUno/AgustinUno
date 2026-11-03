# Profile integration options

Researched 13 October 2026. Updated 3 November 2026.

The design has moved to a single **Gitskin** identity: near-black warm base, red accent `#E0244E`, tight display type, monospace meta. The earlier blue-accent draft and its `#2563EB` banner are gone. Biography, experience, and skills are sourced from the supplied master resume; the vaccine repository link is public; Behance is listed in the resume. Accreditation and internship work are described without assuming public repositories exist.

GitHub READMEs support Markdown and selected HTML rather than a full application UI. No login form or browser extension is needed: [GitHub profile documentation](https://docs.github.com/en/account-and-profile/concepts/personal-profile).

| Integration | Use | Login / setup | Status |
| :--- | :--- | :--- | :--- |
| [Shields.io](https://shields.io/) | Contact badges | No login for these static badges | Not used; contact links are plain text. |
| [Skill Icons](https://github.com/tandpfun/skill-icons) | Technology icons | No login for public embeds | Used at `width="360"` under the banner; theme variants via `<picture>`. |
| [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats) | Repository and language cards | No login for public embeds; self-hosting requires hosting configuration and a GitHub token | Used directly in §05. Public instance is best-effort; maintainers recommend self-hosting or scheduled generation. |
| [GitCity](https://github.com/rishabhbhartiya/GitCity) | Contribution history as an isometric skyline | No login for the hosted instance; self-hosting needs a GitHub token for the GraphQL API | Used in §05 as a linked `api/svg` image, `width="512"`. |
| [Metrics](https://github.com/lowlighter/metrics) | Configurable profile infographic | GitHub Actions and an appropriately scoped token; some plugins need extra credentials | Considered as a future replacement for the multiple cards. |
| [WakaTime README](https://github.com/athul/waka-readme) | Weekly coding-time summaries | WakaTime account, editor integration, and API key saved as a secret | Optional. |
| [Activity Graph](https://github.com/ashutosh00710/github-readme-activity-graph) | Recent contribution graph | No personal login for the public image endpoint | Optional; GitHub already shows a contribution graph. |

External image services remain dependencies even without login. No new accounts, credentials, hosting, or scheduled workflows are configured.

For automation, follow the chosen project's current credential instructions. Store tokens in GitHub Actions secrets, never README URLs or committed files. Prefer fine-grained tokens when supported: [GitHub token documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## Header asset

`assets/header-banner.svg` is a 1200 × 400 hand-generated SVG, committed as text so it stays editable and diffable. It is referenced at `width="100%"` at the top of the README.

Rendering rules that matter if you edit it:

- GitHub renders the file as an `<img>`, so **no external font loads**. The stack is `Segoe UI Variable Display`, `Segoe UI`, `system-ui`, `sans-serif`, with a monospace fallback for the meta lines.
- The generator lives outside the repo; the committed SVG is the source of truth. Keep the `viewBox` if you change the raster size.
- Contrast is tuned for GitHub's dark theme, but the internal background is opaque, so the banner is identical in light mode.

## Skyline embed

```html
<a href="https://gitcity.natrajx.in/AgustinUno">
  <img src="https://gitcity.natrajx.in/api/svg?u=AgustinUno&theme=gold" alt="..." width="512" />
</a>
```

Verified against the live endpoint on 3 November 2026: `200`, `image/svg+xml`, 400 × 296 output.

Two things to know:

1. **`gitskin` is not deployed upstream.** The hosted build accepts `matrix`, `noir`, `aurora`, `ocean`, `gold`, and `ice`. An unknown theme name silently falls back to `matrix` (green), so `theme=gold` — the closest amber — is used for now.
2. **The endpoint is a chain of two third-party services.** `gitcity.natrajx.in` calls `github-contributions-api.jogruber.de` server-side; if either is down, the image breaks. Self-hosting `GitCity/api` removes one hop and enables `theme=gitskin`.

## Repository hygiene

This repository contains its own clone at `GitCity/`, with a separate `.git` and `origin` pointing at `rishabhbhartiya/GitCity`. It is listed in `.gitignore` so it cannot be committed by accident. Options, in order of preference:

1. **Keep it ignored** (current). Zero coupling; the fork lives wherever you put it.
2. **Submodule** — `git submodule add` gives a pinned commit others can fetch. Only worth it if the profile repo should reference that exact revision.
3. **Move it out** to a sibling directory if the profile repo should stay a single-purpose README.

Local commits in the nested clone (for example the `gitskin` theme) are not upstream until a pull request is merged, so they should not be presented as contributions on the profile.

## Other improvements

1. Add screenshots and a short explanation of the problem each project solves — the Claims XML Engine case study in `docs/case-study-claims-xml-engine.md` is the first of these.
2. Feature two or three recent projects that represent the work you want to do, replacing older examples when stronger work is ready.
3. Add a live portfolio link once a real site exists, with short project case studies.
4. Link a public resume when ready; list certifications only when earned.
5. For dependable statistics, generate repository assets on a schedule so the last successful images remain available during outages.

Before publishing, confirm the biography, contact address, and project selection. Review GitHub's README preview in light and dark mode. Language distribution is not a proficiency measure, and public cards do not describe private work.
