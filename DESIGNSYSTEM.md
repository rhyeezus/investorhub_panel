# InvestorHub — Visual Design System (extracted)

**Source:** https://investorhub.com — confirmed as the InvestorHub marketing site (`<title>ASX Investor Relations Software - InvestorHub</title>`, `og:site_name` = InvestorHub).
**Captured:** 4 Nov 2026, Playwright + headless Chromium, viewports 1440×900 (desktop) and 390×844 (mobile).
**Pages crawled:** `/` (home), `/solution` (product), `/blog` (resources index), `/case-studies` (proof), `/book-a-meeting` (form), `/about`. The site has no pricing page.
**Reference screenshots:** `/design-reference/<page>-desktop-1440.png` and `<page>-mobile-390.png` (full page), plus `/design-reference/states/` (hero viewports, open mega-menu, scrolled header, mobile menu, both footers).
**Companion files:** `/src/styles/tokens.css` (CSS custom properties) and `/tailwind.config.snippet.js` (Tailwind theme extension).

**Stack observed:** Next.js on Vercel · Tailwind CSS v4 (CSS-first `@theme` block in `/_next/static/chunks/2_rapv8iyxvm7.css`) · `next/font` for both typefaces · Lucide icons · Lenis smooth scroll · Sanity image CDN · HubSpot analytics (no HubSpot-rendered forms).

**How citations work.** Every value names where it was read:
- `theme` — a custom property in the site's `:root` `@theme` block (source CSS).
- `src .class` — a hand-written class rule in the site CSS.
- `page › selector` — a computed style read in the browser on that page (desktop unless noted). Selectors are abbreviated Tailwind class chains as rendered.

Alpha values are shown as `token/NN` (e.g. `white/60` = `rgba(255,255,255,.6)`); the site produces these with Tailwind's opacity modifier (reported by Chrome as `oklab(... / 0.6)` and converted back to the base token).

---

## 1. Colour

### 1.1 Brand palette (theme tokens)

| Token (theme) | Hex | Role | Where it appears |
|---|---|---|---|
| `--color-neon` | `#00ffb4` | **Brand primary / CTA accent** | Primary button bg (`home › a.rounded-lg.bg-neon` "Book a demo"); highlighted headline words (`home › span.hero-line.font-medium.text-neon`); mega-menu icon strokes (`home › svg.lucide…` 283 strokes site-wide); step numerals `01/02/03` (`home › span.font-mono.text-[38px]`); card eyebrows `text-neon/80` (`case-studies › p.font-mono.text-[11.5px]`); quote marks (`case-studies › div.font-serif.text-[36px].text-neon`); "IH" monogram on blog placeholder thumbs |
| `--color-neon-soft` | `#7affd4` | Softer neon | Defined in theme; **no computed usage found** on the 6 pages |
| `--color-navy` | `#005246` | Deep teal (named "navy") — gradient end, active nav on light pages | Gradient end of every dark band (`home › section#demo … to-[#005246]`); active nav link text on light pages (`blog › button "Resources"` color `#005246`); active-nav pill `bg-navy/10` (light pages) |
| `--color-ink` | `#0b131c` | **Default text** | `body` color on every page; button text on neon; logo + nav on light pages (`blog › svg.text-ink`); with alpha: `ink/70` nav links, `ink/60` footer links, `ink/45` footer tagline, `ink/40` copyright, `ink/10` footer border, `ink/20` mobile-menu scrim |
| `--color-forest` | `#163b31` | **Dark surface** | Dark section bg (`home › div.bg-forest`, `solution › section.bg-forest`, `case-studies`, `about`); nav glass `forest/75` (scrolled, dark pages) and mega-menu panel `forest/75` (dark pages) / `forest/95` (light pages); mobile menu `forest/90`; "Read more" button bg (`case-studies`); active filter pill; `h4` colour; blog eyebrow "Saturday Series"; stat numbers on case-study cards |
| `--color-forest-light` | `#0a7d6a` | **Positive / secondary action** | ▲ delta pills (`home › span.bg-forest-light/10.text-forest-light`); parchment primary button (`solution › a.bg-(--primary)` = `#0a7d6a`, hover `#075a4c`); product-mock icons/bullets (308 fills); `hover:text-forest-light` on legal links |
| `--color-mint` | `#c8e8d8` | Soft green tint | Blog thumbnail placeholder (`blog › div.aspect-[16/10].rounded-2xl.bg-mint`); hero wash radial (`src .hero-wash`, `#c8e8d8` @55%); testimonial band `bg-mint/30` (`case-studies › section.border-y.bg-mint/30`); `bg-mint/50` pill (`about`) |
| `--color-offwhite` | `#eef0f8` | Light neutral | Defined; only `hover:bg-offwhite` utilities exist — **not observed computed** |
| `--color-sky-wash` | `#f0f4fe` | Blue-white wash | Defined (`bg-sky-wash/40` utility exists) — **not observed computed** |
| `--color-slate` | `#374151` | Mock-UI body text | `home › span.text-[10px].text-slate` (product mock labels) |
| `--color-ash` | `#696a72` | Muted body | `book-a-meeting › p.text-[16.5px]` ("Trusted by 280+…"); mock URL bars (`home › span.truncate`) |
| `--color-fog` | `#95959b` | Faint labels | Tiny mono uppercase labels in mocks (`home › p.font-mono.text-[7.5px].uppercase`); "TRUSTED BY IR TEAMS AT" (`book-a-meeting › p.font-mono.text-[11px]`) |
| `--color-steel` | `#6b7280` | Muted UI text | Mock sidebar items; inactive filter pill text (`case-studies › button "United Kingdom"`) |

### 1.2 Surfaces & backgrounds

| Role | Value | Source |
|---|---|---|
| Page canvas | `#fcfcfc` | `body` background-color (all pages) |
| Dark band | `#163b31` (`forest`) | `home › div.relative.isolate.bg-forest` |
| Dark CTA / hero band gradient | `linear-gradient(to bottom right, #0a2a20, #005246)` | `home › section#demo.grain.bg-gradient-to-br.from-[#0a2a20].to-[#005246]`; same on `about` |
| Home hero backdrop | `radial-gradient(58% 48% at 50% 18%, rgba(0,255,180,.14), transparent 68%), linear-gradient(#07150f 0%, #0a1f17 32%, #02493e 70%, #005246 88%)` | `home › section#top div.absolute.inset-0` |
| Light footer / warm neutral | `#f3f1ea` | `blog › footer.bg-[#F3F1EA]`; `case-studies › section.bg-[#f3f1ea]`; case-study carousel cards |
| Form card | `#fafafa` | `book-a-meeting › div.rounded-[32px].bg-[#fafafa]` |
| Parchment page bg | `#f9f6f0` | `solution`/`about › [data-dl-theme=parchment]` wrapper (`--background`) |
| White cards / mocks | `#ffffff` | `home › div.rounded-2xl.bg-white.ring-1.ring-black/[0.06]` |
| Glass card on dark | `white/4` (+ `backdrop-blur(8px)`) | `home › div.problem-card.bg-white/[0.04]`; `case-studies › a.lift.rounded-[var(--radius-card)]` |
| Ghost button on dark | `white/10` | `home › a.rounded-lg.border.border-white/25.bg-white/10` |
| Icon wrap on dark | `white/7` | `home › span.h-8.w-8` (mega-menu) |
| Subtle chip on light | `black/4` – `black/5` | `home › span.rounded-full.bg-black/[0.04]`, `span.bg-black/[0.05]` |

### 1.3 Text colours

| Role | Light surfaces | Dark surfaces | Parchment theme |
|---|---|---|---|
| Headline | `#0b131c` ink (`blog › h3.text-ink`) | `#ffffff` (`home › h1`) | `#2c281f` (`solution › h1`) |
| Body | `#0b131c`; muted `#696a72` ash | `white/70` lead (`home › p.hero-line`), `white/65` (`about › p.text-white/65`), `white/55` (`home › p.text-white/55`) | `#575143` (`solution › p.text-(--muted-foreground)`) |
| Secondary / meta | `slate-600 #45556c` excerpts, `slate-400 #90a1b9` meta (`blog`) | `white/45` menu group heads, `white/40` copyright | `#575143` |
| Eyebrow | `#163b31` (`blog › span "Saturday Series"`), `#95959b` fog | `neon/80`, `white/50` (`home › p "Trusted by 300+…"`) | `#575143` |
| Link | inherits; footer `ink/60 → ink` | `white/60 → white`; `white/75 → white` nav | `#075a4c` (`solution › a "Explore investor hubs"`) |
| Positive | `#0a7d6a` | `#0a7d6a` / neon | `#0a7d6a` (`--hue-green`) |

### 1.4 Borders & rings

| Value | Use | Source |
|---|---|---|
| `1px solid white/10` | Dark panels, dividers (`border-t border-white/10`) | `home › div.rounded-[26px].border-white/10` (mega-menu); footer rule (dark) |
| `1px white/7–8` | Icon wraps, menu CTA row | `home › span.h-8.w-8` |
| `1px white/15–25` | Ghost buttons | `home › a.border-white/25` |
| `ring-1 black/4–8` (box-shadow) | White cards on light | `home › div.ring-black/[0.06]`, `[0.08]`; `case-studies › figure` (`black/4`) |
| `1px ink/10` | Light footer top rule | `blog › footer.border-ink/10` |
| `1px #ebe6db` | Parchment card/button border (`--border`) | `solution › li.rounded-[14px].border` |
| `1px #255341` | Forest-theme mock border | `solution › div.border-(--border)` inside `[data-dl-theme=forest]` |
| `1px black/10` | Search input | `home › input.border-black/10` |
| `2px #fefdfa` | Avatar stacking rings | `solution › span.h-7.w-7` |

### 1.5 Semantic / status colours (observed in product mocks)

| Meaning | Text | Background | Border | Source |
|---|---|---|---|---|
| Positive (bought, growth) | `#0a7d6a` | `forest-light/10` or `#e4ede8` | `#bdd6cd` | `home › span "▲ +38"`; `solution › span "Bought"` |
| Negative (sold) | `#b31e57` (`--hue-rose`), `rose-600 #e70044` in mocks | `#f9e4e5` | `#eebfc6` | `solution › span "Sold"`; `text-rose-600` class on mock svg |
| Warning | `#8a6800` (`--hue-amber`) | `#f0eadf` | `#dacfb6` | `solution › span "Register: not a holder"` |
| Info | `#1f52d0` (`--hue-blue`) | `#e2e9f7` | `#b8ccf2` | `solution › span "Read 2+ announcements"` |
| AI / "Ivy" | `#6b30cf` (`--hue-violet`) | `#f3ecff` (BETA badge) / `#eae6f7` chip | `#cdc4f2` | `solution › span "BETA"`, AI suggestion chips |
| Window chrome dots | — | `#ff5f57` `#febc2e` `#28c840` | — | `home › span.h-2.5.w-2.5.rounded-full.bg-[#ff5f57]` |

Chip tints marked with a plain hex were converted from Chrome's `oklab()` output (±1 in each channel). Tailwind default palette slots kept in the theme: `red-50/300/400/600/700/900`, `amber-50/200/700/800/900`, `emerald-50`, `cyan-50/600` (`#0092b5` seen as a mock icon stroke), `blue-50/200/600`, `rose-600`, `slate-100…600`.

### 1.6 Product-UI themes (shadcn-style variables)

The site ships two scoped themes used inside product mock-ups and whole page sections. Source: `src [data-dl-theme=parchment]` and `src [data-dl-theme=forest]`.

| Variable | Parchment (Solution, About) | Forest (dark mocks) |
|---|---|---|
| `--background` | `#f9f6f0` | `#143629` |
| `--card` | `#fefdfa` | `#0f271f` |
| `--foreground` | `#2c281f` | `#f2fef8` |
| `--muted` / `--muted-foreground` | `#f2ede2` / `#575143` | `#0f271f` / `#9bc0b1` |
| `--secondary` | `#f2ede2` | `#1b4132` |
| `--accent` / `--accent-foreground` | `#e9f3ec` / `#075a4c` | `#164e3a` / `#85ffe2` |
| `--primary` / `--primary-foreground` | `#0a7d6a` / `#f7f4ec` | `#20ffc4` / `#0f271f` |
| `--ring` | `#075a4c` | `#2effd5` |
| `--border` / `--input` | `#ebe6db` / `#ddd7c9` | `#255341` / `#255341` |
| `--hue-green/blue/violet/amber/rose/gray` | `#0a7d6a` `#1f52d0` `#6b30cf` `#8a6800` `#b31e57` `#6d6759` | `#2effd5` `#9db8ff` `#c9a9ff` `#f2c46b` `#ff93b4` `#9bc0b1` |

### 1.7 Gradients & atmospheric effects

| Effect | Definition | Source |
|---|---|---|
| Dark band gradient | `linear-gradient(to bottom right, #0a2a20 0%, #005246 100%)` | `home › section#demo`, `about › section.grain` |
| Blog thumb placeholder | `linear-gradient(to bottom right, #163b31, #005246)` + neon "IH" | `blog › div.bg-gradient-to-br` (136 instances) |
| Light hero wash | `radial-gradient(60% 55% at 50% 0, rgba(0,255,180,.14), transparent 70%), radial-gradient(70% 60% at 50% 38%, rgba(200,232,216,.55), transparent 72%), linear-gradient(#f3fbf7 0%, #fcfcfc 70%)` | `src .hero-wash` (blog, solution) |
| Neon blobs | `.blob` radial neon at 42% / 22% / 16% alpha (`blob-3` is blue `#3c78ff` @18%), 400–820px, `filter: blur(100px)`, `opacity: .45`, drifting 32–52s | `src .blob`, `.blob-1…4` |
| Hero grid | 72px grid of `rgba(255,255,255,.027)` lines, radially masked | `src .hero-grid` |
| Grain | SVG fractal-noise overlay, `opacity: .028`, `mix-blend-mode: overlay` | `src .grain:after` |
| Fades into dark | `linear-gradient(#163b31, transparent)` 260px top/bottom | `home › div.absolute.inset-x-0.top-0.h-[260px]` |
| Accent rule | `h-px bg-gradient-to-r from-neon/70 to-transparent` | `home › span.problem-accent` |
| Neon glow | `--shadow-glow: 0 0 100px -28px rgba(0,255,180,.22)` | `theme`; `src @keyframes loopHubGlow` |
| Blurred product backdrop | screenshot with `filter: blur(9px)` under dark overlay | `book-a-meeting › div.absolute.-inset-8` |
| Photo overlay | `linear-gradient(100deg, rgba(7,16,12,.72) 0%, .45 55%, .2 100%)` | `home › div.absolute.inset-0` over `hub-outback.jpg` |

---

## 2. Typography

### 2.1 Families

| Role | Family | Loaded from | Weights available | Fallback stack (as shipped) |
|---|---|---|---|---|
| Body + headings (`--font-body`, Tailwind `--font-sans` **and** `--font-serif`) | **Momo Trust Sans** | Self-hosted via `next/font/local` → `/_next/static/media/*.woff2`, `font-display: swap`, 3 unicode-range subsets (latin, latin-ext, vietnamese). Typeface by Type Associates (M — N Associates, 2024, SIL OFL 1.1; on Fontsource). | Variable **200–800**, normal only | `ui-sans-serif, system-ui, -apple-system, "Segoe UI", Helvetica, Arial, sans-serif` |
| Accent mono (`--font-mono-accent`, Tailwind `--font-mono`) | **DM Mono** | `next/font/google` (self-hosted woff2 with generated `DM Mono Fallback` size-adjust metrics) | 300, 400, 500 + italics | `"DM Mono Fallback", ui-monospace, "SF Mono", Menlo, monospace` |

Notes: the `font-serif` utility is remapped to the same sans (`theme --font-serif: var(--font-body)…`) and additionally sets `letter-spacing: -.02em; font-weight: 500` (`src .font-serif`). Headings use it. `src .font-mono` also sets `font-feature-settings: "tnum"` + `font-variant-numeric: tabular-nums`.

### 2.2 Weights in use (desktop element counts across 6 pages)

Momo Trust Sans 400 (863) · 500 (339, all headings) · 600 (204, buttons, labels, strong) — no 700+. DM Mono 400 (192) · 500 (160) · 600 (7 — **synthesised**, only 300–500 are loaded).

### 2.3 Type scale (computed at 1440 / 390)

| Role | Desktop | Mobile | Weight | Line-height | Letter-spacing | Family | Source |
|---|---|---|---|---|---|---|---|
| H1 (home) | 52px | 32px | 500 | 1.06 | -0.02em | Momo | `home › h1.font-serif.text-[clamp(32px,4.4vw,52px)].leading-[1.06].tracking-[-0.02em]` |
| H1 (solution / about) | 53–54px | 32–34px | 500 | 1.04–1.05 | -0.02em | Momo | `solution › h1.text-[clamp(32px,3.7vw,54px)]`, `about › h1.text-[clamp(34px,4.2vw,54px)]` |
| H1 (form page) | 44px | 30px | 500 | 1.08 | -0.02em | Momo | `book-a-meeting › h1.text-[clamp(30px,4vw,44px)].leading-[1.08]` |
| H2 large | 44–48px | 30px | 500 | 1.08–1.10 | -0.025em (`tracking-tight`) | Momo | `home › h2.text-[clamp(30px,4.4vw,48px)].leading-[1.1]`, `h2.text-[clamp(30px,4vw,44px)]` |
| H2 standard | 40px | 26–28px | 500 | 1.08–1.10 | -0.02em | Momo | `about › h2.text-[clamp(28px,3vw,40px)]`, `case-studies › h2.text-[clamp(26px,3.4vw,40px)]` |
| H2 blog feature | 34px | 24px | 500 | 1.375 | -0.02em | Momo | `blog › h2.text-[clamp(24px,2.6vw,34px)].leading-snug` |
| H3 | 22px | 22px | 500 | 1.5 | -0.02em | Momo | `home › h3.mt-5.font-serif.text-[22px]` |
| H3 (pillar, dark) | 21px | 21px | 500 | 1.25 | -0.015em | Momo | `about › h3.text-[21px].leading-[1.25].tracking-[-0.015em]` |
| H3 (card title) | 20px | 20px | 500 | 1.375 | -0.025em | Momo | `blog › h3.font-serif.text-xl.leading-snug.tracking-tight` |
| H4 | 14px | 14px | 500 | 1.5 | 0 | Momo (`#163b31`) | `case-studies › h4.text-[14px].font-medium` |
| H5 / H6 | **UNKNOWN** — no `h5`/`h6` rendered on any crawled page | | | | | | |
| Lead paragraph | 18px | 18px | 400 | 1.625 | 0 | Momo | `home › p.hero-line.text-[18px]` (`white/70`), `about › p.text-[18px]` |
| Body large | 16.5–17.5px | same | 400 | 1.55–1.7 | 0 | Momo | `home › p.text-[17px].leading-relaxed`, `about › p.text-[16.5px].leading-[1.7]` |
| Body | 16px / 15px | same | 400 | 1.6 / 1.7 | 0 | Momo | `solution › p.text-[16px].leading-[1.6]`, `about › p.text-[15px].leading-[1.7]` |
| Body small (most common) | 14px | 14px | 400 | 1.625 | 0 | Momo | `blog › p.text-sm.leading-relaxed.text-slate-600`; footer `p.text-[14px]` |
| Caption | 13.5px / 13px / 12.5px / 12px | same | 400 | 1.5 / 1.625 / 1.45 / 1.33 | 0 | Momo | footer links `a.text-[13.5px]`; `case-studies › p.text-[13px].leading-relaxed`; menu `span.text-[12.5px].leading-[1.45]`; `blog › div.text-xs.text-slate-400` |
| Eyebrow / overline | 11–13px | same | 500 | 1.5 | +0.12 – +0.16em, uppercase | **DM Mono** | `home › p.font-mono.font-medium.text-[11.5px].uppercase.tracking-[0.14em]` ("Trusted by 300+…"); `blog › span.font-mono.text-[0.7rem].uppercase` (0.12em); `case-studies › span.font-mono.text-[13px].uppercase.tracking-[0.16em]` |
| Column heading (footer) | 12px | 12px | 600 | 1.5 | +0.14em, uppercase | Momo | `blog › p.text-[12px].font-semibold.uppercase.tracking-[0.14em]` |
| Button | 14 / 15 / 15.5 / 16px | same | 500–600 | 1.5 | 0 | Momo | §5.1 |
| Nav link | 14px | 15px (mobile menu) | 500; 600 active | 1.5 | 0 | Momo | `home › a.rounded-full.px-3.5.py-1.5` |
| Stat numeral | 38–42px | — | 500 | 1.0 | -0.04em | DM Mono (neon) | `home › span.font-mono.font-medium.text-[38px].leading-none.tracking-[-0.04em]`; `span.tabular-nums` 42px |
| Stat (case study) | 32px | 24px | 600 | 1.5 | -0.025em | Momo (`#163b31`) | `case-studies › p.font-serif.text-[clamp(24px,2.6vw,32px)].font-semibold` |
| Pull quote | 23px | 18px (clamp floor) | 400 | ~1.4 | -0.025em | Momo | `case-studies › blockquote.font-serif.text-[clamp(18px,…,23px)]` |
| Mono data | 10–14px | same | 400 | 1.5 | 0 | DM Mono | `solution › dd.font-mono.text-[12px]` ("42,000"); `about › a.font-mono.text-[14px]` (phone) |

### 2.4 Conventions
- Headings: `clamp(min, vw, max)` fluid sizes; always weight 500; tracking -0.015 to -0.025em (stat numerals to -0.05em); leading 1.02–1.12.
- Body: 14–18px, leading 1.5–1.7 (`leading-relaxed` = 1.625 is the default feel).
- Mono is reserved for *data and labels*: tickers, dates, numerals, eyebrows, step numbers, attributions (`case-studies › span.font-mono.text-[12px]` "Stuart Tarrant, CFO…").
- Tracking utilities present: `-0.05 … -0.01em` negatives, `+0.04 … +0.2em` positives; leading utilities `0.75 … 1.9`.

---

## 3. Spacing & layout

| Property | Value | Source |
|---|---|---|
| Site container | **1200px** (`--max-width-site`), `mx-auto max-w-site` — 37 instances, renders 1200 at 1440 | `theme`; `home › div.mx-auto.max-w-site` |
| Horizontal gutter | **32px** desktop (`lg:px-8`), **24px** mobile content (`px-6`), **16px** mobile header (`px-4`) | `home › div.max-w-site.px-6.lg:px-8`; `header.px-4.sm:px-6.lg:px-8` |
| Narrow text measures | 672px (`max-w-2xl`, centred intros), 768px (`max-w-3xl`), 576px (`max-w-xl`), 512px (`max-w-lg`), 620px hero lead, 540/480/460px body columns, 760px H1 | `home › div.reveal.mx-auto.max-w-2xl`; `home › p.max-w-[620px]`; `solution › h1.max-w-[760px]` |
| Section vertical padding (desktop) | 80px (`py-20`), 96px (`py-24`), 112px (`pb-28`), 128px (`lg:py-32`); hero tops 160–176px (`pt-40`, about hero `176/112`) | `solution › section.max-w-site.py-24…` computed 128/128; `about › section` 176/112; `home › div.max-w-site.pt-40` |
| Section vertical padding (mobile) | 56–96px (`py-14`, `py-20`, `py-24`); about hero 144/80 | `solution@mobile › section` 96/96; `about@mobile` 144/80, 96/0 |
| Header | fixed at `top: 16px`; pill `h-[60px]`, full container width, `pl-5 pr-3` (20/12px) | `home › header.top-4 nav.h-[60px].rounded-full.pl-5.pr-3` |
| Footer grid | `md:grid-cols-[1.3fr_2fr] gap-10 lg:gap-16` (64px); inner padding `64px 32px`; bottom bar `mt-12 lg:mt-16 pt-6` | `blog › footer div.grid` |
| Card grids | 2-col feature cards gap 20px (`home` sector cards 560px wide); 3-col blog grid gap ≈20px (cards 365px in 1136px); testimonial masonry = 3 CSS columns with `break-inside-avoid mb-5` | `home › a.rounded-[var(--radius-card)]`; `blog`; `case-studies › figure.break-inside-avoid` |
| Mega-menu | 640px panel, `p-2` (8px), items `p-3 gap-3 rounded-2xl` | `home › div.rounded-[26px].p-2` |
| Base unit | **4px** (`--spacing: .25rem`). Observed value histogram (desktop, all pages): 12, 10, 8, 6, 16, 20, 4, 28, 2, 24, 32, 14, 40, 64, 36, 80, 48, 56, 96, 112, 128, 176 — multiples of 4 dominate; 2/6/10/14 half-steps appear in dense mock UIs | computed `padding/margin/gap` sweep |
| Common scale | 4 · 8 · 12 · 16 · 20 · 24 · 28 · 32 · 40 · 48 · 56 · 64 · 80 · 96 · 112 · 128 | derived from the histogram above |
| Breakpoints | Tailwind v4 defaults: 40rem (640) · 48rem (768) · 64rem (1024) · 80rem (1280) · 96rem (1536); one custom `min-width: 1100px`; `(hover:hover)` and `(pointer:fine)` gates on hover effects | `@media` rules in site CSS |

---

## 4. Shape & depth

### 4.1 Border radius

| Token / value | Use | Source |
|---|---|---|
| `--radius-card` **8px** (`rounded-lg`) | Buttons, dark glass cards, testimonial figures, inputs in mocks | `theme`; `home › a.rounded-lg.bg-neon`; `case-studies › a.rounded-[var(--radius-card)]` |
| **12px** (`rounded-xl`) | Icon wraps, small white cards, search input | `home › span.h-8.w-8` (menu icon); `home › input.rounded-[12px]`; `div.rounded-xl.bg-white.p-3.5` |
| **16px** (`rounded-2xl`) — most used (217) | Product-mock frames, mega-menu items, mobile-menu items, blog thumbs | `home › div.rounded-2xl.bg-white.ring-1`; `blog › div.aspect-[16/10].rounded-2xl` |
| **14px** | Parchment cards, photo figures, carousel arrow buttons | `solution › li.rounded-[14px].border`; `about › figure.rounded-[14px]`; `case-studies › button.h-11.w-11.rounded-[14px]` |
| **10px** | Inner parchment cards | `solution › div.rounded-[10px].border-(--border)` |
| **18px** | Mega-menu footer CTA row | `home › a.rounded-[18px]` |
| **24px** (`rounded-3xl`) | Mobile menu panel | `home@mobile › div.rounded-3xl.p-2` |
| **26px** | Mega-menu panel | `home › div.rounded-[26px]` |
| **28px** | Case-study carousel cards | `case-studies › article.w-[86vw]` |
| **32px** | Booking form card | `book-a-meeting › div.rounded-[32px]` |
| `--radius-feature` **40px** | Defined in theme — **not observed** | `theme` |
| `--radius-pill` **100px** / `rounded-full` | Filter pills, select, nav pill, chips, avatars, step label | `case-studies › button.rounded-[var(--radius-pill)]`; `home › nav.rounded-full` |
| 3–6px | Mini chips and bars inside mocks (`rounded`, `rounded-md`, `rounded-t-[3px]`) | `solution › span.op-rise.rounded-t-[3px]` |

### 4.2 Border widths
1px solid everywhere (204 instances); 2px only for avatar stacking rings and stepper dots (`solution › span.h-7.w-7`). See §1.4 for colours. "Rings" on light cards are `box-shadow: 0 0 0 1px rgba(0,0,0,.04–.08)` (`ring-1 ring-black/[0.06]`).

### 4.3 Shadows

| Token / value | Use | Source |
|---|---|---|
| `--shadow-feather: 0 0 4px -2px rgba(0,0,0,.10)` | Hairline lift on light cards (also `hover:shadow-[var(--shadow-feather)]`) | `theme`; `case-studies › figure` (with `ring-black/4`) |
| `--shadow-feather-strong: 0 0 4px -2px rgba(0,0,0,.25)` | Hover variant | `theme` |
| `--shadow-feature: 0 .36px 1.81px -1.42px rgba(0,0,0,.08), 0 1.37px 6.87px -2.83px rgba(0,0,0,.07), 0 6px 30px -4.25px rgba(0,0,0,.016)` | Feature cards (`hover:shadow-[var(--shadow-feature)]`) | `theme` |
| `--shadow-glow: 0 0 100px -28px rgba(0,255,180,.22)` | Neon halo in hero animation | `theme`; `src @keyframes loopHubGlow` |
| `shadow-sm: 0 1px 3px rgba(0,0,0,.1), 0 1px 2px -1px rgba(0,0,0,.1)` | Nav "Book a demo", search input, inactive filter pills | `home › a.rounded-lg.bg-neon.px-4` |
| Glass panel: `inset 0 1px 0 rgba(255,255,255,.14), 0 28px 60px -20px rgba(11,19,28,.6), 0 4px 14px -6px rgba(11,19,28,.3)` | Mega-menu panel | `home › div.rounded-[26px]` |
| Scrolled nav: `inset 0 1px 0 rgba(255,255,255,.12), 0 12px 34px -12px rgba(11,19,28,.5)` | Header pill after scroll (dark pages) | `home › nav > div.absolute.inset-0` (scrolled) |
| Neon hover glow: `0 8px 32px -6px rgba(0,255,180,.55), 0 0 0 1px rgba(0,255,180,.35)` | `.btn-neon:hover` | `src .btn-neon:hover` (confirmed by hover probe on `book-a-meeting › button.btn-neon`) |
| `shadow-xl` (Tailwind default) | Mobile menu panel | `home@mobile › div.shadow-xl` |
| `drop-shadow(0 2px 3px rgba(44,40,31,.3))` | Cursor icon in solution mock | `solution › svg.drop-shadow-[…]` |

### 4.4 Blur & glass

| Effect | Value | Where | Source |
|---|---|---|---|
| Mega-menu glass | `backdrop-filter: blur(64px) saturate(1.6)` on `forest/75` (dark pages) or `forest/95` (light pages), border `white/10` | Desktop dropdowns | `home › div.[backdrop-filter:blur(64px)_saturate(160%)]`; `blog ›` same with `/95` |
| Scrolled header glass | `blur(24px) saturate(1.5)` on `forest/75`, border `white/10` — only on **dark pages** (header is `fixed`); on light pages the header is `absolute` and simply scrolls away | `home › nav div.backdrop-blur-xl.backdrop-saturate-150` (after 900px scroll) |
| Mobile menu | `blur(24px)` on `forest/90`; scrim `ink/20` | `home@mobile › div.rounded-3xl.backdrop-blur-xl`; `div.fixed.inset-0.bg-ink/20` |
| Glass cards | `blur(8px)` on `white/4` | `home › div.problem-card` |
| Ghost CTA | `blur(8px)` on `white/10` | `home › a.border.border-white/25` |
| Pill on image | `blur(8px)` on `#fefdfa/85` | `solution › span "140 watching"` |
| Ambient blobs | `filter: blur(100px)` | `src .blob` |
| Logo de-emphasis | `grayscale(1) opacity .55–.6` (light) · `brightness(0) invert(1) opacity .8` (dark) | `book-a-meeting › img.grayscale.opacity-55`; `home › img.brightness-0.invert.opacity-80` |

---

## 5. Components

### 5.1 Buttons

| Variant | Tokens | Sizes (font / padding / height) | Hover | Source |
|---|---|---|---|---|
| **Primary — neon** | bg `neon`, text `ink`, `rounded-lg` 8px, weight 600 (500 in header), `shadow-sm` on header size | Header 14px / 10×20 / 41px · Standard 15px / 0×24 / 48px · Hero 15.5px / 14×28 / 51px · Band 16px / 16×32 / 56px | **a)** `.btn-neon`: `translateY(-1px) scale(1.018)` + neon glow shadow (transform .22s, box-shadow .3s); active `scale(.985)`. **b)** utility variant: `bg-neon/90` + `shadow-md`, `transition-all .15–.2s` | `home › a.rounded-lg.bg-neon.px-4`, `a.bg-neon.px-7.py-3.5`, `a.btn-neon.rounded-lg.bg-neon`; `src .btn-neon:hover` |
| **Ghost (on dark)** | bg `white/10` or transparent, border 1px `white/20–25`, text white, `rounded-lg`, weight 500–600, `backdrop-blur(8px)` | 15.5px / 14×28 / 53px · 16px / 16×32 / 58px | bg → `white/15` (utility) or `.btn-ghost`: `translateY(-1px) scale(1.018)` (bg .22s, transform .22s, border .25s) | `home › a.border-white/25.bg-white/10` ("See how it works"); `a.btn-ghost` ("Talk to us first") |
| **Parchment primary** | bg `#0a7d6a`, text `#f7f4ec`, `rounded-lg`, 500 | 14px / 0×20 / 40px · 15px / 12×24 / 47px | bg → `#075a4c` (`transition-colors`) | `solution › a.bg-(--primary)`; `about › a.bg-(--primary).px-6.py-3` |
| **Parchment outline** | bg `#fffefd`, border 1px `#ebe6db`, text `#2c281f` | 14px / 0×20 / 40px | bg → `#f2ede2` | `solution › a.rounded-lg.border` ("See live hubs") |
| **Parchment soft** | bg `#e9f3ec`, text `#075a4c`, arrow icon | 15px / 12×24 / 47px | bg → `#d5e7de`; arrow `translate-x-0.5` | `about › a.bg-(--accent)` ("Read our story") |
| **Forest solid** | bg `forest #163b31`, white, 600, `rounded-lg`, `arrow-up-right` icon | 13px / 8×16 / 36px | bg → `forest-light #0a7d6a` | `case-studies › a "Read more"` |
| **Filter pill** | `rounded-[100px]`, 13.5px/500, 8×16, 36px; active bg `forest` + white; inactive bg white + `steel #6b7280` + `shadow-sm` | — | `transition-all .15s` (inactive→active only) | `case-studies › button "Australia" / "United Kingdom"` |
| **Segmented toggle** | `rounded-[8px] border px-3 py-1.5` 13px; active bg `#fefdfa` border `#ebe6db` text `#2c281f` 500; inactive transparent `#575143` | 34px | text → `#2c281f` | `about › button "Top 20" / "Whole register"` |
| **Icon button** | 44×44 `rounded-[14px]` bg `neon/90`, ink chevron | — | bg → `neon` | `case-studies › button.h-11.w-11` (carousel) |
| **Nav text button** | `rounded-full px-5 py-2.5`, 14px/500, `white/75` | — | text white + bg `white/10` (`transition-all .2s`) | `home › a "Login"` |
| **Disclosure row** | full-width `rounded-lg` bg `white/4`, 16×24, DM Mono 13px uppercase +0.16em, count in `neon/70`, chevron | 52px | bg → `white/7`, ring strengthens | `case-studies › button "View all case studies (14)"` |

Mobile: hero buttons stack full-width within the 24px gutter (`home@mobile › a.bg-neon.px-7` 51px high, ghost below it); header CTA stays 14px / 10×16.

### 5.2 Links
- Base: `a { color: inherit; text-decoration: inherit }` — **no underlines** anywhere observed; colour shifts only, `transition-colors .2s`.
- Footer: `ink/60 → ink` (light) · `white/60 → white` (dark) (`blog › a.text-ink/60.hover:text-ink`).
- Arrow links: `.arrow-link` gap `.375rem → .5rem` on hover (`transition: gap .2s`); utility variant moves the Lucide arrow `group-hover:translate-x-0.5` in .15–.2s (`solution › a "Explore investor hubs"` 14.5px/500 `#075a4c`).
- On dark cards: DM Mono 11–12px uppercase `neon` ("SEE CASE STUDY →"; `home › span.problem-accent` section).
- Legal prose links: `hover: color forest-light` (`src .legal-prose a:hover`).

### 5.3 Header / navigation
- **Shell:** `header` fixed (dark pages) or absolute (light pages), `top: 16px`, `px-4 sm:px-6 lg:px-8`, `z-50`. Inside: `nav` 60px pill (`rounded-full pl-5 pr-3`) spanning the 1200px container.
- **Resting state:** transparent. **Scrolled (dark pages):** an absolutely positioned ring layer fades in (`transition-all .5s ease-out`) to `forest/75` + `blur(24px) saturate(1.5)` + border `white/10` + inset highlight shadow (§4.3).
- **Logo:** inline SVG wordmark (`viewBox 0 0 466 74`), `currentColor` — white on dark, `ink` on light; h-5 (20px) mobile, 22px desktop.
- **Links:** 14px/500, `white/75` (dark) · `ink/70` (light); hover → white / ink. Active = 600 with an animated pill indicator `bg-white/15` (dark) · `bg-navy/10` (light), 33px tall, `px-3.5 py-1.5`. Dropdown triggers show a 14px Lucide chevron (`opacity-60`, rotates `transition-transform .3s ease-out`).
- **Right cluster:** "Login" text button + neon "Book a demo" (header size).
- **Mega-menu:** 640px glass panel (§4.4), `rounded-[26px] p-2`, two columns separated by a `white/10` rule. Group heading 11px uppercase +0.16em `white/45` (`px-3 pt-1 pb-1.5`). Item: `rounded-2xl p-3 gap-3`, 32px icon wrap (`rounded-xl bg-white/7 border-white/8`, neon 16px Lucide icon), title 14px/600 white, description 12.5px `white/55` leading 1.45; hover bg `white/8`. Footer row: `rounded-[18px] bg-white/6 border-white/7 px-4 py-3`, 13.5px (semibold white + `white/60`), arrow icon; hover `white/12` / border `white/15`.
- **Mobile (390):** same pill (358px wide), logo + neon CTA + 40px round hamburger (`aria-label="Open menu"`). Menu panel drops `mt-2`: `rounded-3xl p-2 bg-forest/90 backdrop-blur-xl border-white/10 shadow-xl`, items `rounded-2xl px-4 py-3` 15px/500 `white/80`, active `bg-white/15` 600; sub-groups expand via 39px chevron buttons; page scrim `bg-ink/20`; all `transition .3s ease-out`. See `/design-reference/states/home-mobile-menu-390.png`.

### 5.4 Footer (two variants)
- **Light** (`blog`, `case-studies`, `book-a-meeting`, `about`, `solution`): `bg #f3f1ea`, `border-t ink/10`, inner `max-w-site` padding `64px 32px`; grid `[1.3fr_2fr]` gap 64px; left: logo 24px `ink`, tagline 14px `ink/45` lh 1.625, social links 13.5px `ink/60`, address 13.5px `ink/45` (`address.not-italic`); right: 4 link columns, headings 12px/600 uppercase +0.14em `ink`, links 14px `ink/60 → ink` with `space-y` ~10px; bottom bar `border-t ink/10 mt-12 lg:mt-16 pt-6` with © 13.5px `ink/40` and "Privacy Centre" `ink/55`.
- **Dark** (`home` — rendered inside the CTA gradient band, not a `<footer>` element): identical structure with logo white, headings white, links `white/60 → white`, tagline `white/55`, © `white/40`, privacy `white/50`, rule `white/10`. Partner-logo row (AIRA, ASA, Sohn Hearts & Minds, AMEC, Ignite, RIU, ShareSoc) sits above at 36px tall, `brightness-0 invert opacity-80`.

### 5.5 Cards

| Card | Structure | Tokens | Source |
|---|---|---|---|
| **Glass card (dark)** | number/eyebrow (DM Mono neon) → h3 22px white → p 14.5px `white/55–85` → `h-px` neon gradient rule → mono uppercase neon link | bg `white/4`, `rounded-[var(--radius-card)]` 8px, `p-7/p-8` (28/32px), ring `white/6–8`, `backdrop-blur(8px)`; hover bg `white/6`, ring `white/15`; `.lift:hover translateY(-5px)` (.3s `cubic-bezier(.22,.61,.36,1)`) | `home › div.problem-card`, `a.group.flex.flex-col.rounded-[var(--radius-card)].bg-white/[0.04].p-8`; `case-studies › a.lift` |
| **Product mock frame** | browser chrome (3 dots `#ff5f57/#febc2e/#28c840`, URL pill DM Mono 9.5px `#696a72` on `black/4`) + white app UI, often stacked/offset over a larger frame | bg white, `rounded-2xl` 16px, `ring-1 ring-black/[0.06]`, `overflow-hidden` | `home › div.rounded-2xl.bg-white.ring-1.ring-black/[0.06]` (528px wide); inner `rounded-xl p-3.5 ring-black/[0.08]` |
| **Parchment card** | mock panel on `--muted` header strip → numbered title (DM Mono `01` + h3 22px `#2c281f`) → p 16px `#575143` → divider → check list (Lucide `check` 2.5px `#0a7d6a`, 14.5px) → arrow link `#075a4c` | bg `#fefdfa`, border 1px `#ebe6db`, `rounded-[14px]`, inner `rounded-[10px] p-4` | `solution › li.rounded-[14px].border`, `div.rounded-[10px].border-(--border).bg-(--card)` |
| **Testimonial figure** | 36px neon “ → blockquote 16px/1.5 `ink` → name 14.5px/600 → role DM Mono 12px `fog` | bg white, `rounded-[8px]`, `p-7`, ring `black/4` + feather shadow; masonry columns, `mb-5` | `case-studies › figure.break-inside-avoid.rounded-[var(--radius-card)]` |
| **Case-study carousel card** | left: quote 23px `forest/90` + company 14.5px/600 + role mono 12px `forest/60` + forest button; right: "Challenge" h4 + 13px `forest/65` text + stat 32px/600 `#163b31` + 15px `forest/60` | bg `#f3f1ea`, `rounded-[28px]`, `w-[86vw]` on mobile, `snap-start`; vertical `black/6` divider | `case-studies › article.w-[86vw].snap-start`, `blockquote.font-serif.text-[clamp(18px,…,23px)]` |
| **Blog post card** | thumb `aspect-[16/10] rounded-2xl bg-mint` (image or forest→navy gradient with 24px neon "IH") → eyebrow DM Mono 11.2px/500 +0.12em `#163b31` → title 20px/500 → excerpt 14px `slate-600` `line-clamp-2` → meta 12px `slate-400` "Author · date" | image `transition-transform .5s` (hover scale from `hover:scale-[1.03]` utility — **not triggered in probe**) | `blog › h3.font-serif.text-xl`, `span.mb-2.5.font-mono.text-[0.7rem]`, `div.text-xs.text-slate-400` |
| **Quote card (about)** | 21px/500 lh 1.32 `#075a4c` quote + 12.5px attribution | bg `#e9f3ec`, `rounded-[14px]`, `p-7` | `about › blockquote.rounded-[14px].bg-(--accent).p-7` |
| **Team row** | 56px round photo + name 15px + role 14px `#575143`, `gap-4`, `border-b #ebe6db` | — | `about › li.flex.items-center.gap-4` |
| **Form card** | centred H1 + lead + inline email/CTA group + eyebrow + grey logo ticker | bg `#fafafa`, `rounded-[32px]`, `px-6 py-12`, `max-w-2xl` | `book-a-meeting › div.rounded-[32px].bg-[#fafafa]` |

### 5.6 Badges, pills, chips

| Element | Spec | Source |
|---|---|---|
| Delta pill | DM Mono 8–9px/500, `rounded-full px-1.5 py-px`, `forest-light` on `forest-light/10–12` | `home › span "▲ +38"` |
| Count chip | DM Mono 9px, `rounded-full px-2 py-0.5`, `#696a72` on `black/4` | `home › span "39"` |
| Status chip (parchment) | 11px/400, `rounded-full px-2 py-0.5`, 1px tinted border; colours in §1.5 | `solution › span "Bought" / "Sold" / "Register: not a holder" / "Read 2+ announcements"` |
| BETA badge | 9.5px/500 `#6b30cf` on `#f3ecff`, `rounded-full px-1.5` | `solution › span "BETA"` |
| Avatar initials | 24–28px circle, DM Mono 9.5–10px; `#575143` on `#f2ede2` · `#075a4c` on `#e9f3ec` · `#0a7d6a` on `forest-light/10`; 2px `#fefdfa` ring when stacked | `solution › span.h-7.w-7`; `home › span "FS"` |
| Step label | `rounded-[var(--radius-pill)] px-4 py-2 bg-white/8`, DM Mono uppercase ("01 · ATTRACT") | `home › span.inline-flex.rounded-[var(--radius-pill)]` |
| Mega-menu count / sector select | `rounded-[100px] bg-white/6 py-2.5 pl-4 pr-10` 13.5px/500 white, `appearance-none` + chevron | `case-studies › select#cs-sector` |

### 5.7 Stat / metric blocks
- Hero-band stats: DM Mono 42px/500 `neon` tracking -0.04em (`home › span.tabular-nums` "60%"), label `dd.mt-3 text-[12px] uppercase tracking-[0.12em] font-mono` (`"increase in liquidity*"`), `max-w-[20rem]`.
- Pillar numerals: DM Mono 38px/500 neon `leading-none` (`home › span "01"`).
- Mock KPI tile: title 15px/600 ink → value 18px/600 + delta pill → footnote DM Mono 7.5px uppercase `fog` (`home › p.text-[15px].font-semibold.tracking-tight`).
- Case-study stat: §5.5.

### 5.8 Logo strips / tickers
`.ticker-wrap` (overflow hidden, 80px edge mask) → `.ticker-track` (`width: max-content; animation: ticker 36s linear infinite`, paused on hover). Logos `h-6`/`h-7` (24/28px), `px-7`/`px-10`, `grayscale opacity-55/60` on light (`hover:grayscale-0 hover:opacity-100` utilities present) or `brightness-0 invert opacity-80` on dark. Preceded by a DM Mono eyebrow ("TRUSTED BY IR TEAMS AT", `mb-9`). Sources: `book-a-meeting › div.ticker-wrap`, `about › div.ticker-track`, `home › img.brightness-0.invert`.

### 5.9 Form inputs
- **Search (home):** `input.w-full.rounded-[12px].border.border-black/10.bg-white` 16px, padding `16px 48px 16px 20px`, 58px tall, `shadow-sm`; **focus:** border → `forest/40` (observed via focus probe), no outline ring.
- **Email + CTA group (book-a-meeting):** white container `rounded-[12px]`? (rendered as a 1px `black/10` bordered pill-ish bar with inset neon button), input `h-12 bg-transparent px-4 text-[15px]` with `label.sr-only`; **focus:** browser default outline (`#005fcc auto 1px`) — no custom focus style observed. Includes a hidden honeypot input.
- **Select (case-studies):** see §5.6.
- Focus-visible rings exist as utilities on menu items: `focus-visible:ring-2 focus-visible:ring-forest-light/50`.

### 5.10 Charts & data visuals (inside mocks)
Built in inline SVG/CSS, not a chart library: line chart with dots (`svg viewBox 0 0 400 176`), vertical bars `bg-(--primary)/80 rounded-t-[3px]` animated `scaleY` (`src .op-rise`, `.ev-bar-v`), donut arcs via `stroke-dashoffset` (`src .ev-donut-arc`), register dot-matrix of 20×10 circles (`about ›` fills `#075a4c` top-20 vs muted, `transition-[fill,opacity] .5s`), sparkline in `forest-light`, holder table rows with DM Mono tabular numerals. Palette: `neon`, `forest-light #0a7d6a`, `#3fbf9c` (about dots), `cyan-600 #0092b5`, `rose-600` negatives.

---

## 6. Imagery & iconography

- **Icon set:** **Lucide** (`svg.lucide.lucide-*`, `viewBox 0 0 24 24`, `stroke="currentColor"`, `stroke-width 2`, round caps/joins) — 30–78 icons per page; typical sizes 14px (`h-3.5`) and 16px (`h-4`), 8–10px inside mocks; custom micro-arrows at stroke 2.5–4. Icons in menus sit in 32px `rounded-xl white/7` wraps and are coloured `neon`. Sources: `home › svg.lucide.lucide-messages-square.h-4.w-4`, `svg.lucide.lucide-arrow-right`, `iconHints.lucide` counts.
- **Logo usage (not downloaded):** inline SVG wordmark "InvestorHub" with a leaf/arrow mark, `viewBox 0 0 466 74`, drawn in `currentColor`: white on dark heroes/footer (`home › svg.text-white`), ink on light pages/footer (`blog › svg.text-ink`); 20px (mobile) / 22px (desktop header) / 24px (footer). A mark-only version appears at 16px inside product mocks (`svg.h-[16px]`), and as the favicon `/icon.svg`. Colourways observed: white, ink. A neon "IH" monogram (24px, `font-serif`) stands in for missing blog images.
- **Photography:** real, un-tinted team photography on About (rooftop group, London team, offsite, cooking, sunset, fire-pit) through `next/image`, in `figure.rounded-[14px].overflow-hidden`; 56px circular headshots; one landscape (`/hub-outback.jpg`) used as a hub-mock hero with a dark gradient overlay; a webinar presenter photo on Solution. No stock-photo look; no duotones.
- **Product screenshots:** mostly **HTML/CSS-built mock UIs** (browser chrome + white app surfaces, `rounded-2xl ring-1 ring-black/[0.06]`), stacked and offset (not rotated) and animated; a few real captures as `.webp` (`/mocks/solution/valewind/page.webp`) auto-scrolling inside a frame (`opBrowse 11s`). Book-a-meeting uses a heavily blurred dark screenshot as the backdrop.
- **Illustration style:** none figurative. Abstract data motifs instead — neon node-and-line "circuit" decorations with twinkling dots in the hero (`home › div.ih-stage svg 1440×558`), a faint 72px grid, blurred neon blobs, dot-matrix register, film grain.
- **Client/partner logos:** PNG via Sanity (`/images/yjtji3qs/production/…`) and `/logos/trust/*.png`, shown grey or white (see §5.8).

---

## 7. Motion

| Aspect | Value | Source |
|---|---|---|
| Default transition | `.15s cubic-bezier(.4,0,.2,1)` (Tailwind `--default-transition-*`); colours `.2s`; also `duration-300/500/700/1000` | `theme`; `home › a.transition-colors.duration-200` |
| Signature easing | `cubic-bezier(.22,.61,.36,1)` (soft ease-out) for reveals, hero, lifts, bars; overshoot `cubic-bezier(.34,1.56,.64,1)` in loop keyframes; `ease-out` for menus | `src .reveal`, `.lift`, `.hero-line`, `@keyframes loopFill` |
| Scroll reveal | `.reveal { opacity:0; transform:translateY(24px); transition: opacity .75s, transform .75s }` → `.in` added on intersection; stagger `.reveal-delay-1/2/3` = .1/.2/.3s; `.problem-card` from `translateY(30px) scale(.96)`, `.addon-card` from `28px/.97` | `src .reveal*`; 195 elements across pages |
| Smooth scroll | Lenis (`html.lenis`) | `libs.lenis = true` |
| Hero entrance | `.hero-line`: `heroIn .85s cubic-bezier(.22,.61,.36,1) forwards` from `opacity 0, translateY(18px)`, staggered per line | `src .hero-line`; `home › span.hero-line` |
| Button hover | neon/ghost: `translateY(-1px) scale(1.018)` .22s + glow .3s, active `scale(.985)`; utility buttons: colour/shadow .15–.2s | `src .btn-neon`, `.btn-ghost`; hover probe |
| Card hover | `.lift` `translateY(-5px)` .3s; `.change-tile` `-2px` .2s; glass cards bg/ring .15s; `hover-window` `-8px` .5s | `src .lift:hover`, `.change-tile`, `.hero-window` |
| Link/icon hover | arrow `translate-x-0.5` .15–.2s; `.arrow-link` gap .2s; nav chevron rotate .3s ease-out; nav colour .2s | `home › svg.lucide-arrow-right.transition-transform.duration-200` |
| Menus | mega-menu `origin-top` scale/opacity `.15s ease-out`; header glass ring `.5s ease-out`; mobile menu `.3s ease-out` | `home › div.rounded-[26px]`; `nav > div.transition-all.duration-500` |
| Ambient loops | blobs `drift1/2/3` 32–52s ease-in-out infinite; logo `ticker` 36s linear; testimonial `marqueeY` 42–52s (columns alternate `reverse`, pause on hover); `ihTwinkle` 3s; `ihRipple` 3.2s; `loopSpin` 7s; `evRoute` dash 1.4s; `opBrowse` 11s; hero mock `heroAnx*` sequences (bars .7s, line 1.3s, ping 6s, tooltip 9s) | `src @keyframes …`; computed `animation` sweep |
| Data reveals | bars `scaleY` .8–.95s with per-item delay `calc(var(--i) * 90ms + .2s)`; steps fade/rise .5s ease-out stagger .26s; dots `fill` .5s | `src .op-rise`, `.op-step`, `.ev-bar-v` |
| Reduced motion | `@media (prefers-reduced-motion: reduce)` disables reveal, marquee, twinkle, hero and mock animations (11 rules) | site CSS |

---

## 8. Voice & tone

- **Sentence case, full stops, two-beat headlines.** Headlines read like confident statements, often paired as problem → reframe: "Investor relations was built for twenty people. We're building it for the whole register." (about); "We give you the plan. You make it happen." (solution).
- **One recurring contrast — "top 20" vs "whole register".** It appears in H1s, body copy, footer tagline ("…reaches your whole register, not just the top 20.") and the About dot-matrix visual.
- **Plain, slightly provocative, second person.** "Your company is worth more than the market says." (home CTA band); "Every shareholder, within reach." (about H1). Copy speaks to the company ("you/your register") and assumes capital-markets literacy (register, liquidity, re-rate, holders, catalysts).
- **Proof by number, hedged honestly.** "Trusted by 300+ listed companies across ASX & LSE", "4,772 views on a single CEO letter", "149% increase in hub subscribers", with a mono "*Results may vary." footnote.
- **Low-pressure CTAs and analyst texture.** Primary CTA is always "Book a demo"; secondaries are "Talk to us first", "See how it works", "Read our story", "See live hubs". Numbered pillars (`01 · ATTRACT`), mono tickers (`ASX:AQD`) and timestamps give an operations-dashboard feel rather than marketing gloss.

Example headlines: "Sales and marketing software for investor relations." · "IR software that reaches your whole register" · "See who's getting closer to their entire shareholder base" · "Whatever kind of company you are, we meet you there."

---

## 9. Tailwind theme extension

See `/tailwind.config.snippet.js` (v3-style `theme.extend` reading the variables in `/src/styles/tokens.css`). The live site uses Tailwind v4's CSS-first `@theme`; the equivalent there is to move the `--color-*`, `--font-*`, `--radius-*`, `--shadow-*` declarations from `tokens.css` into an `@theme { … }` block.

---

## 10. Gaps & assumptions

**UNKNOWN / not observed**
- `h5` and `h6` styles — no such elements on any crawled page.
- `--color-neon-soft`, `--color-offwhite`, `--color-sky-wash`, `--radius-feature` (40px) are defined in the theme but no computed usage was found on the six pages; listed for completeness only.
- Hover states that did not trigger in the probe (values taken from source CSS/class names only, so behaviour is inferred from those rules): `.lift` card lift, blog image `hover:scale-[1.03]`, partner-logo `hover:grayscale-0`, `hover:shadow-[0_10px_34px_-10px_rgba(0,…)]` (the full rgba of that arbitrary shadow was truncated in the stylesheet dump → **UNKNOWN**).
- Focus styles: only two observed (search input border `forest/40`; booking email input = browser default outline). Other focus rings are inferred from `focus-visible:ring-*` utilities.
- Mobile hover/focus states: not applicable / not captured.
- Blog article pages, case-study detail pages, `/uk/*` pages and login/app screens were not crawled (no public app screenshot pages exist; product UI is shown via in-page mocks).
- Pull-quote mobile size is given as the `clamp()` floor (18px); the blockquote was not in the mobile sample.
- Exact grid gaps were derived from rendered widths (≈20px) rather than read from a `gap` property on the grid.

**Assumptions / conversions**
- Chrome reports Tailwind v4 opacity colours as `oklab()`; these were mapped back to the base token + alpha (verified: ink, forest, neon, forest-light, mint round-trip exactly). Status-chip tints were converted from `oklab()` to hex and may be ±1 per channel.
- "Section padding" values come from the few `section` elements that carry padding; most bands pad an inner `max-w-site` wrapper instead (`pt-40`, `pb-28`, `py-20`, `py-14`), which is reflected in §3.
- The light-page header being `absolute` (non-sticky) vs. dark-page `fixed` + glass was observed on `blog` vs `home`; assumed to hold for all light vs dark pages.
- DM Mono weight 600 appears in computed styles for 7 elements but only 300/400/500 are loaded — the browser synthesises it; treat 500 as the max intended weight.
- Momo Trust Sans licence (SIL OFL 1.1) and foundry attribution come from Fontsource / the Google Fonts issue tracker, not from the site; verify before reuse.
- Screenshots: `blog-mobile-390` is a JPEG at 1× (page is 58,603px tall; a 2× PNG exceeded the JPEG height limit and weighed 20 MB). All other captures are PNG, mobile at 2×.
- No cookie/consent banner appeared in headless Chromium, so captures are unobstructed.
