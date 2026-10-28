<style>
  @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=VT323&display=swap');
  :root {
    --phosphor: #33ff00;
    --amber: #ffb000;
    --bg: #0d0d0d;
    --scanline: rgba(51,255,0,0.06);
  }
  body { background: var(--bg) !important; color: var(--phosphor) !important; }
  .crt {
    font-family: 'Share Tech Mono', monospace;
    background: linear-gradient(var(--scanline) 50%, transparent 50%);
    background-size: 100% 4px;
    position: relative;
    overflow: hidden;
    padding: 2.5rem 2rem;
    border: 1px solid rgba(51,255,0,0.35);
    border-radius: 0;
    box-shadow: 0 0 30px rgba(51,255,0,0.15), inset 0 0 60px rgba(51,255,0,0.08);
  }
  .crt::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
      0deg,
      rgba(51,255,0,0.06) 0px,
      rgba(51,255,0,0.06) 1px,
      transparent 1px,
      transparent 2px
    );
    pointer-events: none;
    z-index: 10;
  }
  .crt::after {
    content: '_';
    animation: blink 1s step-end infinite;
    color: var(--phosphor);
    font-weight: bold;
    margin-left: 2px;
  }
  @keyframes blink { 50% { opacity: 0; } }
  .crt h1, .crt h2, .crt h3 { font-family: 'VT323', monospace; letter-spacing: 0.08em; text-transform: uppercase; color: var(--phosphor); }
  .crt .banner { font-family: 'VT323', monospace; color: var(--phosphor); white-space: pre; line-height: 1.1; font-size: 1.05rem; opacity: 0.95; text-shadow: 0 0 8px rgba(51,255,0,0.6); }
  .crt .prompt { color: var(--amber); font-weight: bold; }
  .crt a { color: var(--phosphor); text-decoration: underline; text-decoration-color: var(--amber); text-underline-offset: 3px; }
  .crt a:hover { color: var(--amber); background: rgba(255,176,0,0.1); }
  .crt .sub { opacity: 0.75; font-size: 0.9em; }
  .crt .divider { border: 0; border-top: 1px dashed rgba(51,255,0,0.3); margin: 1.5rem 0; }
  .crt kbd { border: 1px solid rgba(51,255,0,0.45); padding: 0.15rem 0.35rem; background: rgba(51,255,0,0.08); color: var(--phosphor); font-family: 'Share Tech Mono', monospace; font-size: 0.8em; border-radius: 2px; }
</style>

<div class="crt" markdown="1">

```
███████╗███████╗██╗  ██╗██╗███████╗███╗   ██╗ ██████╗██╗      █████╗
██╔════╝██╔════╝██║  ██║██║██╔════╝████╗  ██║██╔═══██╗    ██╔══╝
██║     █████╗  ██║  ██║██║█████╗  ██╔██╗ ██║██║   ██║    █████╗
██║     ██╔══╝  ███████║██║██╔══╝  ██║╚██╗██║██║   ██║    ██╔══╝
╚███████╗███████╗██║  ██║██║███████╗██║ ╚████║╚██████╔╝    ███████╗
 ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝     ╚══════╝
```

```
##### terminal :: CRT phosphor 2026 #####
```

<span class="prompt">$</span> STATUS: AVAILABLE FOR HIRE <span class="prompt">>> </span>LINKEDIN: /in/justine-lloyd-bautista-666432228 <span class="prompt">>> </span>BEHANCE: /lloydbautista <span class="prompt">>> </span>EMAIL: justinelloydgbautista.pupsj@gmail.com

> <span class="prompt">>> </span>**Design-driven full-stack engineer** shipping data-critical internal tools for a PhilHealth-accredited health IT provider.

<span class="sub">9+ years in visual design | 50,000+ rows per run | 2,000+ healthcare units served</span>

---

### <span class="prompt">$</span> GITCITY SKYLINE // GITSKIN THEME

<a href="https://gitcity.natrajx.in/AgustinUno?theme=gitskin"><img src="https://gitcity.natrajx.in/api/svg?u=AgustinUno&theme=gitskin" alt="AgustinUno GitCity Skyline — Gitskin theme" width="100%" /></a>

---

### <span class="prompt">$</span> `01` EXPERIENCE

<span class="prompt">>> </span>**Eurolink Network International Corp.** — Software Developer — 2026

<kbd>Internal MIS</kbd> <kbd>NDA</kbd>

- Shipped production internal tools for the **ENIC MIS suite** at one of seven PhilHealth-accredited HITPs in the Philippines, serving 2,000+ healthcare units nationwide.
- **Claims XML Data Engine:** a web-native validation tool processing 50,000+ rows per run; resolved a Chromium memory overflow via binary-level optimization and browser thread management for zero-lag financial accuracy.
- **Real-Time Collaborative Notes:** a Notion-style multi-user interface built with Tiptap, Yjs, and SignalR, with RBAC and live caret tracking.

<span class="prompt">>> </span>**PUP San Juan — QA Office** — Full-Stack Developer — 2023–2026

<kbd>University Systems</kbd>

- Led full-stack development, UI/UX architecture, and technical support for digital accreditation workflows, streamlining document evaluation cycles across the university.

<span class="prompt">>> </span>**GLITCH & Student Council** — VP for Comms & Lead Designer — 2022–Present

<kbd>Leadership</kbd> <kbd>Brand</kbd>

- Directed visual identity, creative teams, and campaign systems for 3 consecutive years at GLITCH and for the PUPSJ Student Council, alongside independent client work.

---

### <span class="prompt">$</span> `02` SELECTED WORK

<span class="prompt">>> </span>**ENIC Healthcare MIS Suite**

<sub><kbd>ASP.NET Core (.NET 10)</kbd> <kbd>SignalR</kbd> <kbd>Tiptap</kbd> <kbd>Yjs</kbd> <kbd>XML</kbd></sub>

Proprietary internal MIS modules built for large-scale hospital reimbursement validation and real-time cross-department documentation.

<sub><b>Featured</b> — Proprietary production system — under NDA</sub>

---

<span class="prompt">>> </span>**PUPSJ-CON — Accreditation Platform**

<sub><kbd>Laravel</kbd> <kbd>PostgreSQL</kbd> <kbd>Tailwind CSS</kbd> <kbd>Figma</kbd></sub>

Led a 5-member team as PM, Lead UI/UX, and Full-Stack Developer, digitizing institutional accreditation with RBAC, server-side search, and automated document workflows.

<sub>Best Capstone Awardee — PUP San Juan</sub>

---

<span class="prompt">>> </span>**YAKAP — Partner Platform Identity**

<sub><kbd>Figma</kbd> <kbd>Design Systems</kbd> <kbd>Typography</kbd> <kbd>Brand</kbd></sub>

Designed two competing comprehensive visual identity systems and typography guidelines for a PhilHealth-integrated partner platform pitched to executive leadership.

<sub><a href="https://www.behance.net/lloydbautista"><b>View design portfolio on Behance →</b></a></sub>

---

<span class="prompt">>> </span>**Project V — Vaccine Management**

<sub><kbd>Java</kbd> <kbd>PHP</kbd> <kbd>MySQL</kbd></sub>

Desktop and backend vaccination tracking platform built to resolve scheduling and record bottlenecks, awarded **Top 1 Best Project** at the Asia Pacific College bootcamp cohort.

<sub><a href="https://github.com/AgustinUno/vaccine-management-system-2021"><b>View repository →</b></a></sub>

<p align="right">
  <sub><a href="https://github.com/AgustinUno?tab=repositories"><b>Explore all public repositories →</b></a></sub>
</p>

---

### <span class="prompt">$</span> `03` STACK & TOOLING

<p align="center"><b>APPLICATION DEVELOPMENT</b></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=ts,js,php,java,react,tailwind,laravel,dotnet&theme=dark&perline=4" />
    <img src="https://skillicons.dev/icons?i=ts,js,php,java,react,tailwind,laravel,dotnet&theme=light&perline=4" alt="TypeScript, JavaScript, PHP, Java, React, Tailwind CSS, Laravel, and .NET" />
  </picture>
</p>

<p align="center"><b>DATA & INFRASTRUCTURE</b></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=postgres,mysql,git,docker,linux,debian&theme=dark&perline=6" />
    <img src="https://skillicons.dev/icons?i=postgres,mysql,git,docker,linux,debian&theme=light&perline=6" alt="PostgreSQL, MySQL, Git, Docker, Linux, and Debian" />
  </picture>
</p>

<p align="center"><b>DESIGN & PROTOTYPING</b></p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://skillicons.dev/icons?i=figma,ps,ai,ae,blender&theme=dark&perline=5" />
    <img src="https://skillicons.dev/icons?i=figma,ps,ai,ae,blender&theme=light&perline=5" alt="Figma, Photoshop, Illustrator, After Effects, and Blender" />
  </picture>
</p>

---

### <span class="prompt">$</span> `04` HONORS & CERTIFICATIONS

<span class="prompt">>> </span>**PUP San Juan, Sept 2026.** Magna Cum Laude (GPA 1.2 — PH scale, 1.0 is highest) — Rank 1 Overall IT Graduate — Rank 3 Overall Campus — Junior Programmer of the Year — Best Capstone — Public Service Award.

<span class="prompt">>> </span>**Trend Micro Capture The Flag, Oct 2025.** Ranked 80th nationwide in Linux exploitation and defensive security against university and professional teams.

<span class="prompt">>> </span>**AWS Cloud Club Solar Power Hackathon, July 2025.** Cloud infrastructure planning and technical builder (Team TLP).

<details>
  <summary><b>Certifications & systems background</b></summary>
  <br />
  <ul>
    <li><b>Certifications:</b> Lean Six Sigma Yellow Belt — Fortinet Certified Associate in Cybersecurity — FortiGate 7.6 Operator — Cisco Cyber Threat Management — Salesforce Supported Virtual Internship — DTI Graphic Design for SMB & Marketing.</li>
    <li><b>Quality assurance & systems:</b> 50,000+ record dataset validation, boundary and edge-case testing, REST/API validation, Linux (Debian 13, RHEL, Arch, Sway WM), Cisco and Fortinet firewalls.</li>
  </ul>
</details>

---

### <span class="prompt">$</span> `05` ACTIVITY

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=AgustinUno&show_icons=true&hide_border=true&theme=github_dark&hide_rank=true&title_color=2563EB&icon_color=2563EB" />
    <img height="165" src="https://github-readme-stats.vercel.app/api?username=AgustinUno&show_icons=true&hide_border=true&theme=default&hide_rank=true&title_color=2563EB&icon_color=2563EB" alt="Justine's public GitHub repository statistics" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=AgustinUno&layout=compact&hide_border=true&theme=github_dark&langs_count=6&title_color=2563EB" />
    <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=AgustinUno&layout=compact&hide_border=true&theme=default&langs_count=6&title_color=2563EB" alt="Language distribution across public repositories" />
  </picture>
  <br />
  <sub><i>Production healthcare MIS work is hosted in private enterprise repositories under NDA. Public metrics reflect open-source and academic repositories.</i></sub>
</div>

<br />

<div align="center">
  <p><b>Have a role, system architecture challenge, or design project in mind?</b></p>
  <p><a href="mailto:justinelloydgbautista.pupsj@gmail.com"><b>Let's talk →</b></a></p>
</div>

</div>
