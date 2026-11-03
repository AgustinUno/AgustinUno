// Deterministic generator for assets/header-banner.svg
import fs from "node:fs";

const W = 1200, H = 400, R = 20;
const INK = "#0A090B";
const INK_WARM = "#100B0E";
const RED = "#E0244E";
const RED_HOT = "#FF6B84";
const TEXT = "#F8F3F2";
const MUTED = "#B9A6AB";
const BUILDING = "#191219";
const BUILDING_ALT = "#1E151C";
const WINDOW = "#33222B";

let seed = 0x51f3c7;
const rnd = () => {
  seed = (seed * 1664525 + 1013904223) >>> 0;
  return seed / 0x100000000;
};
const pick = (a, b) => a + rnd() * (b - a);
const rint = (a, b) => Math.floor(pick(a, b + 1));

// ---- skyline --------------------------------------------------------------
const BASE = 400;
const city = [];
let x = -30;
while (x < W + 30) {
  const w = rint(16, 52);
  const h = rint(30, 132);
  city.push({ x, w, h });
  x += w + rint(4, 12);
}

const buildings = city
  .map(({ x, w, h }, i) => {
    const top = BASE - h;
    const body = i % 4 === 0 ? BUILDING_ALT : BUILDING;
    const out = [`<rect x="${x}" y="${top}" width="${w}" height="${h}" fill="${body}"/>`];
    out.push(
      `<rect x="${x}" y="${top}" width="${w}" height="1.5" fill="#3A2A33" opacity="${(0.35 + rnd() * 0.4).toFixed(2)}"/>`
    );
    // sparse windows, a few lit warm
    const cols = Math.max(1, Math.floor((w - 6) / 8));
    const rows = Math.max(1, Math.floor((h - 10) / 11));
    const ox = (w - (cols * 8 - 3)) / 2;
    for (let c = 0; c < cols; c++) {
      for (let r = 0; r < rows; r++) {
        const roll = rnd();
        if (roll > 0.88) {
          const lit = roll > 0.975 ? RED_HOT : WINDOW;
          const op = roll > 0.975 ? (0.5 + rnd() * 0.4).toFixed(2) : "0.75";
          out.push(
            `<rect x="${(x + ox + c * 8).toFixed(1)}" y="${(top + 7 + r * 11).toFixed(1)}" width="2.6" height="4" fill="${lit}" opacity="${op}"/>`
          );
        }
      }
    }
    return out.join("");
  })
  .join("");

const antennas = city
  .map((b, i) => ({ ...b, i }))
  .sort((a, b) => b.h - a.h)
  .slice(0, 3)
  .map((b) => {
    const cx = (b.x + b.w / 2).toFixed(1);
    return (
      `<rect x="${(b.x + b.w / 2 - 0.6).toFixed(1)}" y="${BASE - b.h - 16}" width="1.2" height="16" fill="#2A1E26"/>` +
      `<circle cx="${cx}" cy="${BASE - b.h - 17}" r="1.5" fill="${RED}" opacity="0.75"/>`
    );
  })
  .join("");

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="title desc">
  <title id="title">Justine Lloyd Bautista — Software Developer and UI/UX &amp; Visual Designer, Philippines</title>
  <desc id="desc">Dark banner with a short red rule above the name, the role and availability in muted text, and a low city skyline rising along the bottom edge.</desc>

  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="${INK}"/>
      <stop offset="0.55" stop-color="${INK}"/>
      <stop offset="1" stop-color="${INK_WARM}"/>
    </linearGradient>
    <radialGradient id="ember" cx="0.74" cy="1" r="0.55">
      <stop offset="0" stop-color="${RED}" stop-opacity="0.30"/>
      <stop offset="0.38" stop-color="#8E1230" stop-opacity="0.14"/>
      <stop offset="1" stop-color="${RED}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="haze" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="${INK}" stop-opacity="0"/>
      <stop offset="1" stop-color="#1A1016" stop-opacity="0.55"/>
    </linearGradient>
    <clipPath id="frame"><rect width="${W}" height="${H}" rx="${R}"/></clipPath>
  </defs>

  <g clip-path="url(#frame)">
    <rect width="${W}" height="${H}" fill="url(#bg)"/>
    <rect x="0" y="200" width="${W}" height="200" fill="url(#haze)"/>
    <rect width="${W}" height="${H}" fill="url(#ember)"/>

    <g stroke="#FFFFFF" stroke-opacity="0.022" stroke-width="1">
      ${Array.from({ length: 14 }, (_, i) => `<path d="M${(i + 1) * 86} 0V${BASE}"/>`).join("")}
    </g>

    <g>${buildings}${antennas}</g>
    <rect x="0" y="${BASE - 2}" width="${W}" height="2" fill="${RED}" opacity="0.22"/>
  </g>

  <!-- accent rule -->
  <rect x="80" y="86" width="72" height="5" rx="2.5" fill="${RED}"/>

  <!-- meta column, top right -->
  <g font-family="ui-monospace,'Cascadia Mono','SF Mono',Menlo,Consolas,monospace" text-anchor="end">
    <text x="1120" y="92" font-size="13" font-weight="500" letter-spacing="5.2" fill="${MUTED}" opacity="0.62">PHILIPPINES</text>
    <text x="1120" y="120" font-size="11" font-weight="600" letter-spacing="3.6" fill="${RED}" opacity="0.85">AVAILABLE FOR WORK</text>
  </g>

  <g font-family="'Segoe UI Variable Display','Segoe UI',system-ui,-apple-system,'Helvetica Neue',Arial,sans-serif">
    <text x="78" y="186" font-size="68" font-weight="700" letter-spacing="-1.7" fill="${TEXT}">Justine Lloyd Bautista</text>
    <text x="80" y="230" font-size="23" font-weight="400" letter-spacing="0.3" fill="${MUTED}">Software Developer · UI/UX &amp; Visual Designer</text>
  </g>
</svg>
`;

fs.writeFileSync(process.argv[2], svg, "utf8");
console.log(`written ${svg.length} bytes, ${city.length} buildings`);
