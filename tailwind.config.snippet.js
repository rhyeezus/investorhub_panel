/**
 * Tailwind theme extension mirroring /src/styles/tokens.css
 * (InvestorHub design tokens, extracted 4 Nov 2026 — see /DESIGNSYSTEM.md).
 *
 * Tailwind v3: merge `theme.extend` into tailwind.config.js and import
 * `src/styles/tokens.css` before your Tailwind layers. Colours use the
 * `rgb(var(--x-rgb) / <alpha-value>)` form so opacity modifiers work
 * (e.g. `bg-neon/90`, `text-white/60`, `border-forest/40`).
 *
 * Tailwind v4: the site itself uses CSS-first config — move the
 * `--color-*`, `--font-*`, `--radius-*`, `--shadow-*` declarations from
 * tokens.css into an `@theme { … }` block instead of using this file.
 */
const withAlpha = (rgbVar) => `rgb(var(${rgbVar}) / <alpha-value>)`;

/** @type {import('tailwindcss').Config['theme']['extend']} */
const extend = {
  colors: {
    neon: { DEFAULT: withAlpha('--color-neon-rgb'), soft: 'var(--color-neon-soft)' },
    navy: withAlpha('--color-navy-rgb'),
    ink: withAlpha('--color-ink-rgb'),
    forest: {
      DEFAULT: withAlpha('--color-forest-rgb'),
      light: withAlpha('--color-forest-light-rgb'),
      deep: 'var(--color-forest-deep)',
    },
    mint: withAlpha('--color-mint-rgb'),
    offwhite: 'var(--color-offwhite)',
    'sky-wash': 'var(--color-sky-wash)',
    slate: { DEFAULT: 'var(--color-slate)', 400: '#90a1b9', 600: '#45556c' },
    ash: 'var(--color-ash)',
    fog: 'var(--color-fog)',
    steel: 'var(--color-steel)',
    canvas: 'var(--color-canvas)',
    sand: 'var(--color-sand)',
    'card-soft': 'var(--color-card-soft)',
    positive: { DEFAULT: 'var(--color-positive)', bg: 'var(--color-positive-bg)', border: 'var(--color-positive-border)' },
    negative: { DEFAULT: 'var(--color-negative)', bg: 'var(--color-negative-bg)', border: 'var(--color-negative-border)', strong: 'var(--color-negative-strong)' },
    warning: { DEFAULT: 'var(--color-warning)', bg: 'var(--color-warning-bg)', border: 'var(--color-warning-border)' },
    info: { DEFAULT: 'var(--color-info)', bg: 'var(--color-info-bg)', border: 'var(--color-info-border)' },
    ai: { DEFAULT: 'var(--color-ai)', bg: 'var(--color-ai-bg)', border: 'var(--color-ai-border)' },
    parchment: {
      bg: 'var(--parchment-background)',
      card: 'var(--parchment-card)',
      fg: 'var(--parchment-foreground)',
      muted: 'var(--parchment-muted)',
      'muted-fg': 'var(--parchment-muted-foreground)',
      accent: 'var(--parchment-accent)',
      'accent-fg': 'var(--parchment-accent-foreground)',
      'accent-hover': 'var(--parchment-accent-hover)',
      primary: 'var(--parchment-primary)',
      'primary-hover': 'var(--parchment-primary-hover)',
      'primary-fg': 'var(--parchment-primary-foreground)',
      border: 'var(--parchment-border)',
      input: 'var(--parchment-input)',
      outline: 'var(--parchment-outline-bg)',
    },
  },

  fontFamily: {
    sans: ['"Momo Trust Sans"', 'ui-sans-serif', 'system-ui', '-apple-system', '"Segoe UI"', 'Helvetica', 'Arial', 'sans-serif'],
    serif: ['"Momo Trust Sans"', 'ui-sans-serif', 'system-ui', 'sans-serif'], // site maps serif → same sans
    mono: ['"DM Mono"', '"DM Mono Fallback"', 'ui-monospace', '"SF Mono"', 'Menlo', 'monospace'],
  },

  fontSize: {
    display: ['var(--text-display)', { lineHeight: '1.06', letterSpacing: '-0.02em', fontWeight: '500' }],
    'display-lg': ['var(--text-display-lg)', { lineHeight: '1.05', letterSpacing: '-0.02em', fontWeight: '500' }],
    h1: ['var(--text-h1)', { lineHeight: '1.08', letterSpacing: '-0.02em', fontWeight: '500' }],
    'h2-lg': ['var(--text-h2-lg)', { lineHeight: '1.1', letterSpacing: '-0.025em', fontWeight: '500' }],
    h2: ['var(--text-h2)', { lineHeight: '1.1', letterSpacing: '-0.02em', fontWeight: '500' }],
    'h2-sm': ['var(--text-h2-sm)', { lineHeight: '1.375', letterSpacing: '-0.02em', fontWeight: '500' }],
    h3: ['22px', { lineHeight: '1.5', letterSpacing: '-0.02em', fontWeight: '500' }],
    'h3-sm': ['20px', { lineHeight: '1.375', letterSpacing: '-0.025em', fontWeight: '500' }],
    h4: ['14px', { lineHeight: '1.5', fontWeight: '500' }],
    lead: ['18px', { lineHeight: '1.625' }],
    'body-lg': ['17px', { lineHeight: '1.625' }],
    body: ['16px', { lineHeight: '1.6' }],
    'body-sm': ['14px', { lineHeight: '1.625' }],
    caption: ['13.5px', { lineHeight: '1.5' }],
    'caption-sm': ['12.5px', { lineHeight: '1.45' }],
    eyebrow: ['11.5px', { lineHeight: '1.5', letterSpacing: '0.14em', fontWeight: '500' }],
    'eyebrow-wide': ['13px', { lineHeight: '1.5', letterSpacing: '0.16em', fontWeight: '500' }],
    'column-heading': ['12px', { lineHeight: '1.5', letterSpacing: '0.14em', fontWeight: '600' }],
    button: ['15px', { lineHeight: '1.5', fontWeight: '600' }],
    'button-sm': ['14px', { lineHeight: '1.5', fontWeight: '500' }],
    'button-lg': ['16px', { lineHeight: '1.5', fontWeight: '600' }],
    nav: ['14px', { lineHeight: '1.5', fontWeight: '500' }],
    stat: ['42px', { lineHeight: '1', letterSpacing: '-0.04em', fontWeight: '500' }],
    'stat-sm': ['38px', { lineHeight: '1', letterSpacing: '-0.04em', fontWeight: '500' }],
    quote: ['var(--text-quote)', { lineHeight: '1.4', letterSpacing: '-0.025em' }],
  },

  letterSpacing: {
    display: '-0.02em',
    stat: '-0.04em',
    eyebrow: '0.14em',
    'eyebrow-wide': '0.16em',
    'eyebrow-tight': '0.12em',
  },

  lineHeight: { display: '1.06', heading: '1.1', body: '1.6', loose: '1.7' },

  maxWidth: {
    site: 'var(--max-width-site)',      // 1200px
    prose: 'var(--max-width-prose)',    // 672px
    lead: 'var(--max-width-lead)',      // 620px
    column: 'var(--max-width-column)',  // 540px
    h1: 'var(--max-width-h1)',          // 760px
    menu: 'var(--menu-width)',          // 640px
  },

  spacing: {
    gutter: 'var(--gutter-desktop)',          // 32px
    'gutter-sm': 'var(--gutter-mobile)',      // 24px
    section: 'var(--section-y)',              // 96px
    'section-sm': 'var(--section-y-sm)',      // 80px
    'section-lg': 'var(--section-y-lg)',      // 128px
    'section-hero': 'var(--section-y-hero)',  // 160px
    header: 'var(--header-height)',           // 60px
  },

  borderRadius: {
    card: 'var(--radius-card)',         // 8px  — buttons, dark cards
    panel: 'var(--radius-panel)',       // 14px — parchment cards, figures
    'menu-row': 'var(--radius-menu-row)', // 18px
    menu: 'var(--radius-menu)',         // 26px — mega-menu
    carousel: 'var(--radius-carousel)', // 28px
    'form-card': 'var(--radius-form-card)', // 32px
    feature: 'var(--radius-feature)',   // 40px (site token, unused)
    pill: 'var(--radius-pill)',         // 100px
  },

  boxShadow: {
    feather: 'var(--shadow-feather)',
    'feather-strong': 'var(--shadow-feather-strong)',
    feature: 'var(--shadow-feature)',
    glow: 'var(--shadow-glow)',
    glass: 'var(--shadow-glass)',
    'nav-scrolled': 'var(--shadow-nav-scrolled)',
    'neon-hover': 'var(--shadow-neon-hover)',
    'ring-light': 'var(--ring-light)',
    'ring-light-strong': 'var(--ring-light-strong)',
    'ring-dark': 'var(--ring-dark)',
  },

  backdropBlur: { card: '8px', nav: '24px', menu: '64px' },
  backdropSaturate: { nav: '1.5', menu: '1.6' },
  blur: { blob: '100px' },

  backgroundImage: {
    'dark-band': 'var(--gradient-dark-band)',
    'blog-thumb': 'var(--gradient-blog-thumb)',
    'hero-home': 'var(--gradient-hero-home)',
    'hero-wash': 'var(--gradient-hero-wash)',
    'accent-rule': 'var(--gradient-accent-rule)',
    'fade-forest': 'var(--gradient-fade-forest)',
  },

  transitionDuration: { 220: '220ms', 750: '750ms', 850: '850ms' },
  transitionTimingFunction: {
    reveal: 'cubic-bezier(0.22, 0.61, 0.36, 1)',
    overshoot: 'cubic-bezier(0.34, 1.56, 0.64, 1)',
  },

  keyframes: {
    heroIn: { to: { opacity: '1', transform: 'none' } },
    ticker: { '0%': { transform: 'translateX(0)' }, '100%': { transform: 'translateX(-50%)' } },
    marqueeY: { '0%': { transform: 'translateY(0)' }, '100%': { transform: 'translateY(-50%)' } },
    drift1: { '0%,100%': { transform: 'translate(0) scale(1)' }, '50%': { transform: 'translate(55px,40px) scale(1.06)' } },
    drift2: { '0%,100%': { transform: 'translate(0) scale(1)' }, '50%': { transform: 'translate(-45px,30px) scale(.95)' } },
    drift3: { '0%,100%': { transform: 'translate(0) scale(1)' }, '50%': { transform: 'translate(30px,-45px) scale(1.04)' } },
    shimmer: { to: { backgroundPosition: '-200% 0' } },
  },
  animation: {
    'hero-in': 'heroIn 850ms cubic-bezier(0.22, 0.61, 0.36, 1) forwards',
    ticker: 'ticker 36s linear infinite',
    'marquee-y': 'marqueeY 46s linear infinite',
    'drift-1': 'drift1 38s ease-in-out infinite',
    'drift-2': 'drift2 44s ease-in-out infinite',
    'drift-3': 'drift3 52s ease-in-out infinite',
  },
};

module.exports = { theme: { extend } };
