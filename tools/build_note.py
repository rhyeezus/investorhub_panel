#!/usr/bin/env python3
"""Build the one-page note as an HTML page in the CRM's own design system.

Reads docs/review-and-plan.md, pulls the embedded fonts and design tokens from the original
branch file, and writes crm/5 - Review and plan.html. Re-run after editing the markdown.
"""
import re, sys, pathlib
import markdown

HERE = pathlib.Path(__file__).parent
orig = (HERE.parent / "crm" / "3 - Corella CRM - Branch (engineer's version).html").read_text(encoding="utf-8")

fonts = "\n".join(re.findall(r'@font-face\{[^}]*\}', orig))
tokens = re.search(r':root \{.*?\n\}', orig, re.S).group(0)

md = (HERE.parent / "docs" / "review-and-plan.md").read_text(encoding="utf-8")
title = re.match(r'# (.+)', md).group(1)
body_md = md.split("\n", 1)[1]
body = markdown.markdown(body_md, extensions=["smarty"])

# Byline and the link to the prototype are part of the page, not the note text.
BYLINE = 'Rhys Gourley · Product Builder panel · 5 November 2026'
PROTOTYPE = "4 - Corella CRM - Branch (reviewed).html"

html = f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
{fonts}
</style>
<style>
{tokens}

* {{ box-sizing: border-box; }}
html, body {{ margin: 0; }}
body {{
  background: var(--background); color: var(--foreground);
  font-family: var(--font-sans); font-size: 14.5px; line-height: 1.5;
  font-synthesis: none; -webkit-font-smoothing: antialiased;
}}
a {{ color: var(--accent-foreground); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
b, strong, h1, h2, h3 {{ font-weight: 500; }}

.nav {{ display: flex; align-items: center; gap: 24px; max-width: 980px; margin: 0 auto; padding: 14px 24px; }}
.chip {{ display: flex; align-items: center; gap: 10px; padding: 6px 12px 6px 6px; border: 1px solid var(--border); border-radius: 9999px; background: var(--card); font-size: 13px; font-weight: 500; white-space: nowrap; }}
.chip .logo {{ width: 24px; height: 24px; border-radius: 9999px; background: var(--accent); color: var(--accent-foreground); display: grid; place-items: center; font-size: 11px; }}
.badge {{ display: inline-flex; align-items: center; gap: 5px; font-size: 12px; font-weight: 500; padding: 1px 9px; border-radius: 9999px; white-space: nowrap; line-height: 1.6; --h: var(--hue-green); background: color-mix(in oklab, var(--h) 12%, var(--card)); border: 1px solid color-mix(in oklab, var(--h) 30%, var(--card)); color: var(--h); }}
.badge .dot {{ width: 7px; height: 7px; border-radius: 9999px; background: var(--h); display: inline-block; }}
.nav .grow {{ flex: 1; }}
.btn {{ font: inherit; font-size: 13.5px; font-weight: 500; border-radius: var(--radius); padding: 7px 14px; border: 1px solid var(--primary); background: var(--primary); color: var(--primary-foreground); white-space: nowrap; display: inline-flex; align-items: center; gap: 6px; }}
.btn:hover {{ background: color-mix(in oklab, var(--primary) 88%, black); text-decoration: none; }}

.page {{ max-width: 980px; margin: 0 auto; padding: 0 24px 40px; }}
.card {{ background: var(--card); border: 1px solid var(--border); border-radius: calc(var(--radius) + 4px); box-shadow: 0 1px 2px rgba(44,40,31,.04), 0 8px 24px rgba(44,40,31,.04); overflow: hidden; }}
.card-head {{ padding: 26px 36px 20px; border-bottom: 1px solid var(--border); }}
.eyebrow {{ font-family: var(--font-mono); font-size: 11.5px; font-weight: 500; letter-spacing: .08em; text-transform: uppercase; color: var(--muted-foreground); }}
.card-head h1 {{ font-size: 28px; line-height: 1.2; margin: 6px 0 4px; letter-spacing: -.01em; }}
.card-head .sub {{ color: var(--muted-foreground); font-size: 13.5px; }}

.body {{ padding: 8px 36px 28px; columns: 2; column-gap: 40px; column-rule: 1px solid var(--border); }}
.body h2 {{ font-size: 12px; font-family: var(--font-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted-foreground); margin: 26px 0 8px; break-after: avoid; }}
.body h2:first-child {{ margin-top: 18px; }}
.body p {{ margin: 0 0 10px; }}
.body ul, .body ol {{ margin: 0 0 10px; padding-left: 20px; }}
.body li {{ margin-bottom: 5px; }}
.body li::marker {{ color: var(--muted-foreground); font-family: var(--font-mono); font-size: 12px; }}
.body > * {{ break-inside: avoid; }}

.foot {{ max-width: 980px; margin: 0 auto; padding: 0 24px 30px; display: flex; justify-content: space-between; color: var(--muted-foreground); font-size: 12px; }}

@media (max-width: 820px) {{ .body {{ columns: 1; }} }}

@media print {{
  @page {{ size: A4; margin: 10mm 11mm; }}
  body {{ background: #fff; font-size: 10.4px; line-height: 1.4; }}
  .nav, .foot, .btn {{ display: none; }}
  .page {{ padding: 0; max-width: none; }}
  .card {{ border: 0; box-shadow: none; border-radius: 0; }}
  .card-head {{ padding: 0 0 8px; }}
  .card-head h1 {{ font-size: 20px; }}
  .body {{ padding: 4px 0 0; column-gap: 28px; }}
  .body h2 {{ margin: 14px 0 5px; font-size: 10px; }}
  .body p, .body ul, .body ol {{ margin-bottom: 7px; }}
  .body li {{ margin-bottom: 3px; }}
}}
</style>
</head>
<body data-dl-theme="parchment">
<nav class="nav">
  <div class="chip"><span class="logo">CF</span>Corella Finance</div>
  <span class="badge"><span class="dot"></span>Review and plan</span>
  <span class="grow"></span>
  <a class="btn" href="{PROTOTYPE}">Open the prototype</a>
</nav>
<main class="page"><div class="card">
  <div class="card-head">
    <div class="eyebrow">Organisations in the CRM · one week left in the cycle</div>
    <h1>{title}</h1>
    <div class="sub">{BYLINE}</div>
  </div>
  <div class="body">
{body}
  </div>
</div></main>
<footer class="foot"><span>All people, firms and figures are fictional, as in the pack.</span><span>Print this page for the PDF.</span></footer>
</body>
</html>
"""

out = HERE.parent / "crm" / "5 - Review and plan.html"
out.write_text(html, encoding="utf-8")
print("wrote", out, len(html), "bytes")
