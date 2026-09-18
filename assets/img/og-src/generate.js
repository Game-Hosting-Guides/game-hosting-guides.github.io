const fs = require('fs');
const sharp = require('sharp');

const logoB64 = fs.readFileSync(require('path').join(__dirname, '..', 'logo.jpg')).toString('base64');

// Brand tokens
const C = {
  cream: '#fbfaf6',
  ink: '#14130f',
  muted: '#5e5b54',
  amber: '#c08a14',
  amberStrong: '#a07210',
  gold: '#f5b82e',
  wash: '#fbf2dc',
  dark: '#1f1d18',
  hairline: '#d9d4c3',
};

const SERIF = 'Playfair Display';
const SANS = 'Inter Variable, DejaVu Sans';

// Circle-clipped logo, centered at (cx, cy) with radius r
function logo(cx, cy, r, id) {
  const d = r * 2;
  return `
  <clipPath id="clip${id}"><circle cx="${cx}" cy="${cy}" r="${r * 0.97}"/></clipPath>
  <image x="${cx - r}" y="${cy - r}" width="${d}" height="${d}" clip-path="url(#clip${id})"
    href="data:image/jpeg;base64,${logoB64}"/>`;
}

// Dark rating pill centered at (cx, cy)
function chip(cx, cy, w, h, label, fontSize) {
  return `
  <rect x="${cx - w / 2}" y="${cy - h / 2}" width="${w}" height="${h}" rx="${h / 2}" fill="${C.ink}"/>
  <text x="${cx}" y="${cy}" dominant-baseline="central" text-anchor="middle"
    font-family="${SANS}" font-size="${fontSize}" font-weight="600" fill="${C.gold}">${label}</text>`;
}

function topRule() {
  return `<rect x="0" y="0" width="1200" height="5" fill="${C.amber}"/>`;
}

function bg() {
  return `<rect width="1200" height="630" fill="${C.cream}"/>`;
}

// Shared header for interior pages: small logo + small-caps brand
function header(id) {
  return `
  ${logo(88, 84, 27, id)}
  <text x="130" y="84" dominant-baseline="central" font-family="${SANS}" font-size="19"
    font-weight="600" letter-spacing="3.5" fill="${C.ink}">GAME HOSTING GUIDES</text>
  <line x1="60" y1="130" x2="1140" y2="130" stroke="${C.hairline}" stroke-width="1.5"/>`;
}

function footer(leftText) {
  return `
  <line x1="60" y1="540" x2="1140" y2="540" stroke="${C.hairline}" stroke-width="1.5"/>
  <text x="60" y="581" font-family="${SANS}" font-size="19" font-weight="400" fill="${C.muted}">${leftText}</text>
  <text x="1140" y="581" text-anchor="end" font-family="${SANS}" font-size="19" font-weight="600"
    letter-spacing="1" fill="${C.amberStrong}">gamehostingguides.com</text>`;
}

function kicker(text, y = 196) {
  return `<text x="60" y="${y}" font-family="${SANS}" font-size="17" font-weight="600"
    letter-spacing="3" fill="${C.amberStrong}">${text}</text>`;
}

const svgs = {};

/* ---------- 1. og-default: centered cover ---------- */
svgs['og-default'] = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630">
${bg()}
${topRule()}
${logo(600, 143, 47, 'D')}
<text x="600" y="243" text-anchor="middle" font-family="${SANS}" font-size="18" font-weight="600"
  letter-spacing="4.5" fill="${C.amberStrong}">INDEPENDENT &#183; EDITORIAL &#183; HANDS-ON</text>
<text x="600" y="345" text-anchor="middle" font-family="${SERIF}" font-size="86" font-weight="700"
  fill="${C.ink}">Game Hosting Guides</text>
<line x1="540" y1="388" x2="660" y2="388" stroke="${C.hairline}" stroke-width="1.5"/>
<text x="600" y="438" text-anchor="middle" font-family="${SANS}" font-size="27" font-weight="400"
  fill="${C.muted}">Independent Minecraft server hosting reviews</text>
${chip(600, 505, 190, 54, '&#9733;&#160; 9.0 / 10', 24)}
<text x="600" y="585" text-anchor="middle" font-family="${SANS}" font-size="18" font-weight="600"
  letter-spacing="1.5" fill="${C.amberStrong}">gamehostingguides.com</text>
</svg>`;

/* ---------- 2. og-comparison: ranked ---------- */
svgs['og-comparison'] = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630">
${bg()}
${topRule()}
${header('C')}
${kicker('REVIEWED &amp; RANKED &#183; DISCLOSED HARDWARE')}
<text x="60" y="288" font-family="${SERIF}" font-size="76" font-weight="700" fill="${C.ink}">Best Minecraft Server</text>
<text x="60" y="378" font-family="${SERIF}" font-size="76" font-weight="700" fill="${C.ink}">Hosting <tspan fill="${C.amber}">2026</tspan></text>
<text x="60" y="463" dominant-baseline="central" font-family="${SANS}" font-size="21" font-weight="600" fill="${C.muted}">#1</text>
${chip(180, 463, 150, 50, '&#9733;&#160; 9.0', 23)}
<text x="300" y="463" dominant-baseline="central" font-family="${SANS}" font-size="21" font-weight="600" fill="${C.muted}">#2</text>
${chip(420, 463, 150, 50, '&#9733;&#160; 8.7', 23)}
<text x="540" y="463" dominant-baseline="central" font-family="${SANS}" font-size="21" font-weight="600" fill="${C.muted}">#3</text>
${chip(660, 463, 150, 50, '&#9733;&#160; 8.5', 23)}
${footer('Ranked from hands-on testing — performance, support &amp; value')}
</svg>`;

/* ---------- 3. og-reviews ---------- */
svgs['og-reviews'] = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630">
${bg()}
${topRule()}
${header('R')}
${kicker('HANDS-ON TESTING &#183; TRANSPARENT SCORING')}
<text x="60" y="288" font-family="${SERIF}" font-size="76" font-weight="700" fill="${C.ink}">In-depth Minecraft</text>
<text x="60" y="378" font-family="${SERIF}" font-size="76" font-weight="700" fill="${C.ink}">Host Reviews</text>
${chip(165, 463, 210, 56, '&#9733;&#160; 9.0 / 10', 25)}
<text x="300" y="463" dominant-baseline="central" font-family="${SANS}" font-size="22" font-weight="400"
  fill="${C.muted}">Every host scored across performance, support &amp; value</text>
${footer('Real servers, real benchmarks — no pay-to-win rankings')}
</svg>`;

/* ---------- 4. og-guides ---------- */
const guideItem = (x, num, label) => `
<text x="${x}" y="463" dominant-baseline="central" font-family="${SANS}" font-size="22" font-weight="700" fill="${C.amber}">${num}</text>
<text x="${x + 42}" y="463" dominant-baseline="central" font-family="${SANS}" font-size="22" font-weight="500" fill="${C.ink}">${label}</text>`;

svgs['og-guides'] = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630">
${bg()}
${topRule()}
${header('G')}
${kicker('SETUP &#183; PERFORMANCE &#183; MODPACKS')}
<text x="60" y="288" font-family="${SERIF}" font-size="76" font-weight="700" fill="${C.ink}">Minecraft Server</text>
<text x="60" y="378" font-family="${SERIF}" font-size="76" font-weight="700" fill="${C.ink}">Hosting Guides</text>
${guideItem(60, '01', 'Choose a host')}
<line x1="310" y1="448" x2="310" y2="478" stroke="${C.hairline}" stroke-width="1.5"/>
${guideItem(345, '02', 'Set up your server')}
<line x1="645" y1="448" x2="645" y2="478" stroke="${C.hairline}" stroke-width="1.5"/>
${guideItem(680, '03', 'Optimize &amp; scale')}
${footer('Step-by-step tutorials, from first join to peak TPS')}
</svg>`;

/* ---------- render ---------- */
const outDir = '/home/olle/projects/game-hosting-guides/assets/img';
const srcDir = outDir + '/og-src';
fs.mkdirSync(srcDir, { recursive: true });

(async () => {
  for (const [name, svg] of Object.entries(svgs)) {
    fs.writeFileSync(`${srcDir}/${name}.svg`, svg);
    await sharp(Buffer.from(svg)).png().toFile(`${outDir}/${name}.png`);
    const m = await sharp(`${outDir}/${name}.png`).metadata();
    console.log(name, m.width, m.height);
  }
})();
