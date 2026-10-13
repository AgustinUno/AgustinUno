# Profile integration options

Researched on 13 October 2026.

The design uses a restrained blue accent, a centered introduction, direct contact links, real project links, and grouped skill icons with light/dark variants. Biography, experience, and skills were updated from the user's supplied master resume. The vaccine repository link was found on the public profile; Behance is listed in the resume. Accreditation and internship work are described without assuming public repositories exist. The placeholder portfolio link, visitor counter, and old Heroku streak endpoint were removed. Existing local image files were preserved.

GitHub READMEs support Markdown and selected HTML rather than a full application UI. No login form or browser extension is needed: [GitHub profile documentation](https://docs.github.com/en/account-and-profile/concepts/personal-profile).

| Integration | Use | Login / setup | Recommendation |
| :--- | :--- | :--- | :--- |
| [Shields.io](https://shields.io/) | Contact badges | No login for these static badges | Included; keep the row short. |
| [Skill Icons](https://github.com/tandpfun/skill-icons) | Technology icons | No login for public embeds | Included with alternative text and theme variants. |
| [GitHub Readme Stats](https://github.com/anuraghazra/github-readme-stats) | Repository and language cards | No login for public embeds; self-hosting requires hosting configuration and a GitHub token | Included in a collapsible section. The public instance is best-effort; the maintainers recommend self-hosting or GitHub Actions generation for reliability. |
| [Metrics](https://github.com/lowlighter/metrics) | Configurable profile infographic | GitHub Actions and an appropriately scoped token; some plugins need extra credentials | Consider as a future replacement for multiple cards. |
| [WakaTime README](https://github.com/athul/waka-readme) | Weekly coding-time summaries | WakaTime account, editor integration, and API key saved as a secret | Optional if you want to publish tracked coding time. |
| [Activity Graph](https://github.com/ashutosh00710/github-readme-activity-graph) | Recent contribution graph | No personal login for the public image endpoint | Optional; GitHub already displays a contribution graph. |

External image services remain dependencies even without login. No new accounts, credentials, hosting, or scheduled workflows have been configured.

For automation, follow the chosen project's current credential instructions. Store tokens in GitHub Actions secrets, never README URLs or committed files. Prefer fine-grained tokens when supported: [GitHub token documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## Header asset

`assets/header-banner.svg` is an editable 1600 × 500 landscape placeholder. Replace it with your finished banner at the same path, or update the README image path for a PNG export. The contact badges sit beneath it in a horizontal row and may wrap on narrow screens. GitHub activity cards are visible directly, without a dropdown.

## Other improvements

1. Add screenshots, setup instructions, and a short explanation of the problem each project solves.
2. Feature two or three recent projects that represent the work you want to do, replacing older examples when stronger work is ready.
3. Add a live portfolio link once a real site exists, with short project case studies.
4. Link a public resume when ready; list certifications only when earned.
5. For dependable statistics, generate repository assets on a schedule so the last successful images remain available during outages.

Before publishing, confirm the biography, learning topics, contact address, and project selection. Review GitHub's README preview in light and dark mode. Language distribution is not a proficiency measure, and public cards do not describe private work.
