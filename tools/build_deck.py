#!/usr/bin/env python3
"""Build preview/presentation.html: the panel talk-through as a slide deck in
InvestorHub's own design language (src/styles/tokens.css), with the CRM's
embedded fonts so it works offline from a double-click.

Slides are plain <section> blocks in SLIDES below. Re-run after editing.
Keys in the deck: → / space / PageDown next, ← / PageUp back, N toggles notes,
O shows the overview grid, Esc closes it. Hash in the URL remembers the slide.
"""
import re, pathlib

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
crm = (ROOT / "crm" / "3 - Corella CRM - Branch (engineer's version).html").read_text(encoding="utf-8")
fonts = "\n".join(re.findall(r'@font-face\{[^}]*\}', crm))
tokens = (ROOT / "src" / "styles" / "tokens.css").read_text(encoding="utf-8")

SHOT = "../docs/screenshots/"

def img(name, alt):
    return f'<figure class="shot"><img src="{SHOT}{name}" alt="{alt}" loading="eager"></figure>'

# --------------------------------------------------------------------------
# Slides. `dark` for section openers, `light` for content. `notes` is what to say.
# --------------------------------------------------------------------------
SLIDES = []
def slide(kind, body, notes="", label=""):
    SLIDES.append(dict(kind=kind, body=body, notes=notes, label=label))

# 1
slide("dark", """
<div class="eyebrow">Product Builder panel · 5 November 2026</div>
<h1>Organisations in the CRM<span class="accent">.</span></h1>
<p class="lead">How I understood the problem, what I found in the week-1 build, what I built instead, and what I'd fix in the five days left.</p>
<p class="byline">Rhys Gourley</p>
""", notes="Fifteen minutes. I'll show the thinking, not just the result. Problem first, then what I found, then what I built and how it changed as I tested it.", label="Title")

# 2
slide("light", """
<div class="eyebrow">How I worked</div>
<h2>Problem first. Then the files. Then build, test, change.</h2>
<ol class="steps">
  <li><b>Read the brief before the solution.</b> I deliberately didn't look at the pitch's answer until I'd written down the problem in my own words.</li>
  <li><b>Used both CRMs like Josh would.</b> Today, then the branch. Wrote down everything I couldn't do.</li>
  <li><b>Built on their CRM file,</b> in their design system, so it opens with a double-click.</li>
  <li><b>Audited my own build four times</b> and changed it each time. That's most of what I'll show you.</li>
</ol>
<p class="muted">Two briefs arrived: the pack asked for a plan, the email for a prototype and a note. I followed the email and folded the plan in.</p>
""", notes="The brief discrepancy, once, lightly. Then move on.", label="How I worked")

# 3
slide("light", """
<div class="eyebrow">The problem, in my words</div>
<h2>Josh doesn't want to work out of the spreadsheet. The CRM should be the source of truth.</h2>
<div class="cols">
  <div>
    <p>A fund manager is a team, and Josh meets, plans and reports by the team. The CRM only knows people. So the institutional side lives in a sheet, and when Corella asked us to load it, we couldn't.</p>
    <p>Manual entry in a free-text field is how this happens. It's inevitable that's going to be wrong.</p>
  </div>
  <div class="who">
    <div><span class="k">Customer</span>Corella Finance. The deal waited on this.</div>
    <div><span class="k">Users</span>Josh and Hannah, investor relations.</div>
    <div><span class="k">In between</span>Customer success. They're close to clients and will run the clean-up for the ones who won't.</div>
    <div><span class="k">Not just Corella</span>38 clients have invented their own "institution" tag, spelled 11 ways. Two prospects didn't buy because of it. One of them said: "we'd keep our spreadsheet".</div>
  </div>
</div>
""", notes="Say the source-of-truth line. That's the frame for everything else. Josh's own email: 'load it so we can run everything from there'.", label="Problem")

# 4
slide("light", """
<div class="eyebrow">What I found in the branch</div>
<h2>I couldn't find the feature. Then I found three Larkspurs.</h2>
<div class="cols">
  <div class="quotes">
    <blockquote>"I'm not seeing any way to add an individual to an organisation."</blockquote>
    <blockquote>"There's currently no way to edit the organisation."</blockquote>
    <blockquote>"You're editing the user, not the organisation. That's a disconnect."</blockquote>
  </div>
  <div>
    <p>Organisations was a checkbox inside Contacts. Grouping by it gave 18 "firms" for 9: Larkspur Capital, Larkspur Capital Mgmt and LCM, each with its own people.</p>
    <p>A meeting logged on a firm took attendees as free text and never reached the people.</p>
    <p class="test"><b>The pitch's test:</b> Josh opens Larkspur, sees Priya, David and Tom with their roles, logs the August roadshow once. <b>None of the three steps worked.</b></p>
  </div>
</div>
""", notes="These are my notes from the walkthrough, verbatim. The point isn't that Jimmy got it wrong; it's that I only understood why once I asked what an organisation actually was in the data.", label="What I found")

# 5
slide("dark", """
<div class="eyebrow">The diagnosis</div>
<h2>It was built as a label. The pitch needs a record.</h2>
<div class="cols">
  <div class="card glass">
    <div class="eyebrow">A label</div>
    <p>The firm's name is a bit of text typed into each person's record. The CRM doesn't know Larkspur exists. It only knows three people have similar words in a box. Fix one, the other two don't follow.</p>
  </div>
  <div class="card glass neon">
    <div class="eyebrow">A record</div>
    <p>Larkspur exists once, like a contact does. Each person is linked to it. Rename it and everyone follows. Anything underneath inherits the change. A meeting logged on it stays with it.</p>
  </div>
</div>
<p class="lead">Every problem I'd listed came back to this one thing. Make the firm a record and the rest is assembly.</p>
<p class="muted">Kept from week 1: the audit line when a person's firm changes, and the import mapping the company column. Good instincts, both.</p>
""", notes="One cause, several symptoms. For Jimmy: not 'the UI is wrong' but 'the firm is text on each person, and it needs to be a thing of its own that people link to'. Then credit what he did well.", label="Diagnosis")

# 6
slide("light", """
<div class="eyebrow">The idea</div>
<h2>Separate the two. Merge the duplicates. Never type a firm again.</h2>
<ul class="idea">
  <li><b>Contacts and Organisations are two lists.</b> Each links to the other.</li>
  <li><b>Select the duplicates, merge them, pick which name is the master.</b> Everyone and everything moves across. The old names are kept, for data integrity and so the next import lands in the right place.</li>
  <li><b>A human confirms every merge.</b> The account owner or customer success. They have the context to know LCM is Larkspur. The system doesn't.</li>
  <li><b>Pick a firm from a list, never type one.</b> Creating a new one is a deliberate step.</li>
  <li><b>Log a meeting once on the firm, tick who was there.</b> It shows on each of them.</li>
</ul>
""", notes="This is the design, in the order I arrived at it. The merge flow I described before I'd seen a single screen of it.", label="The idea")

# 7
slide("light", """
<div class="eyebrow">The bet</div>
<h2>If a firm is a record and the clean-up is suggest-then-confirm, Josh will trust the CRM over his sheet.</h2>
<div class="cols">
  <div class="card warn">
    <div class="eyebrow">What I can't tell from the outside</div>
    <p>In my prototype, logging a meeting once and seeing it on three people was easy. In the real product it may not be: the pack suggests a meeting sits against one person. If so, this is a bigger change than it looks.</p>
    <p><b>That's the first thing I'd want to understand with Jimmy.</b> It decides whether days 2 to 3 are a day or a week.</p>
  </div>
  <div>
    <div class="eyebrow">What I'm assuming</div>
    <ul>
      <li>CS will run the clean-up for clients who won't.</li>
      <li>A firm is the right unit this cycle. Funds within a firm are the next bet, as the pitch says.</li>
      <li>Suggesting duplicates by name is enough for now. The pitch rules out guessing from email addresses.</li>
    </ul>
  </div>
</div>
""", notes="Say what I can't see from the outside before anyone asks. I built it in a mock, so I don't know how hard the real version is. That's a question, not a claim.", label="The bet")

# 8
slide("dark", """
<div class="eyebrow">What I built</div>
<h2>In their file, on their design system, clickable.</h2>
<p class="lead">Four screens, then the four rounds of changes that got it here.</p>
<p class="muted">crm / 4 - Corella CRM - Branch (reviewed).html</p>
""", notes="Switch to the prototype tab and do the next two slides live. The screenshots are the fallback.", label="Built")

# 9
slide("light", """
<div class="eyebrow">Organisations, and the clean-up</div>
<h2>Eighteen firms. Five likely duplicates. Nothing merges until someone says so.</h2>
<div class="cols wide">
  """ + img("r2-01-orgs-top.png", "Organisations list with a notice of five likely duplicates") + """
  <div>
    <p>A real list, in the nav. The notice is a soft prompt, not an error. Open it, hit Merge on the Larkspur row, choose the name to keep.</p>
    """ + img("r4-merge-dialog-crop.png", "Merge dialog: which name do we keep?") + """
  </div>
</div>
""", label="Screens 1")

# 10
slide("light", """
<div class="eyebrow">The firm, and the test</div>
<h2>Open Larkspur. Tick who was there. It's on Priya's timeline.</h2>
<div class="cols wide">
  """ + img("r3-org-page.png", "Larkspur Capital: people with roles and the timeline") + """
  <div>
    <p>Priya, David, Tom and Ella with the roles Josh's sheet already had. Log the roadshow once with the three of them ticked, open Priya: <i>With Larkspur Capital: David Okafor, Priya Raman, Tom Avery</i>.</p>
    <p class="big"><b>The pitch's test, passing.</b></p>
  </div>
</div>
""", notes="Pause here. This is what the whole review builds to.", label="Screens 2")

# 11
slide("light", """
<div class="eyebrow">Four rounds</div>
<h2>What I noticed, and what changed.</h2>
<table class="t rounds">
  <tr><th>I wrote down</th><th>So I changed</th></tr>
  <tr><td>"The dropdown's going to get blown out. There's no search."</td><td>One searchable picker for choosing a firm and for adding people. Nothing is created until you save.</td></tr>
  <tr><td>"Merge selected is all the way at the top. It's disconnected."</td><td>An action bar on the table that appears when rows are ticked.</td></tr>
  <tr><td>"Log meeting twice is gratuitous."</td><td>One Log meeting, collapsed until you need it.</td></tr>
  <tr><td>"Set, that's bad. Make it an action: add to organisation."</td><td>A proper button, on the person and on every row of the contacts list.</td></tr>
  <tr><td>"Back to contacts is a button. I'd use breadcrumbs."</td><td>Breadcrumbs. The three header buttons went.</td></tr>
  <tr><td>"Not the browser's pop-up. A message in the product."</td><td>Inline confirmations that say what's kept and what's lost.</td></tr>
  <tr><td>"If I create a duplicate it should tell me in the flow."</td><td>New organisation checks the name as you type, then goes straight to adding people.</td></tr>
  <tr><td>"I'm not sure what the import template is doing for us."</td><td>Pulled it. It belongs with the importer, which is next cycle.</td></tr>
</table>
""", notes="Every row is a line from my own audit notes. Four passes, each one through the whole flow as Josh. The last one was an accessibility pass: eleven violation types down to zero.", label="Four rounds")

# 12
slide("light", """
<div class="eyebrow">What I didn't build, and why</div>
<h2>Thin on purpose.</h2>
<div class="grid2">
  <div class="card"><h3>Josh's spreadsheet</h3><p>The second problem, bigger than this one. The importer keys on email and his sheet has names. The failing import is left visible on purpose.</p></div>
  <div class="card"><h3>The pitch's own "not this cycle"</h3><p>Linking firms to the ownership report, reporting per firm, firms shared across clients.</p></div>
  <div class="card"><h3>Nice, not now</h3><p>Organisation type (fund manager, broker, super fund), an owner per firm, follow-ups with a done status, permissions.</p></div>
  <div class="card"><h3>A written summary per firm</h3><p>I wanted it. A canned one in a prototype would be a fake, so it waits for real data.</p></div>
</div>
""", notes="Being explicit about what's not built is discipline, not gaps. The summary one: I argued for it and then talked myself out of it.", label="Left out")

# 13
slide("light", """
<div class="eyebrow">The five days</div>
<h2>In order, because each one needs the last.</h2>
<ol class="days">
  <li><span class="d">Day 1</span><span><b>Organisation as a record.</b> Contacts point at it. Everything depends on this.</span></li>
  <li><span class="d">Day 1 to 2</span><span><b>The migration with the review screen</b>, so the data is right before CS or Josh see it.</span></li>
  <li><span class="d">Day 2 to 3</span><span><b>The firm's page.</b> People with roles, log a meeting with attendees. The "done looks like" test.</span></li>
  <li><span class="d">Day 3</span><span><b>Organisations list with merge.</b></span></li>
  <li><span class="d">Day 4</span><span><b>The contact side.</b> Picker, role, links.</span></li>
  <li><span class="d">Day 5</span><span><b>Walk CS through it. Fix what they find.</b></span></li>
</ol>
<p class="muted">How we'd know: Josh logs the February roadshow on firms, not in the sheet. The Funds tab stops being updated. CS stop hearing "can't group by firm". Corella first; wrong merges stop the rollout.</p>
""", notes="If Jimmy's schema answer is bad, days 2 to 3 stretch and 4 to 5 compress. Say that.", label="Five days")

# 14
slide("light", """
<div class="eyebrow">What I'd want to understand</div>
<h2>Enough to judge scope and feasibility. Three for Jimmy, three for Josh.</h2>
<div class="cols">
  <div>
    <div class="eyebrow">Jimmy</div>
    <ul>
      <li>Organisation is a text field on each person today. Is making it a proper record a small change or a big one?</li>
      <li>A meeting seems to live on one person. How hard is it to have it on a firm and on the people who were there?</li>
      <li>Across other clients, how messy is the company field? That tells us whether the clean-up is a one-off or a feature.</li>
    </ul>
  </div>
  <div>
    <div class="eyebrow">Josh</div>
    <ul>
      <li>Does he have an email for everyone in his sheet? The import seems to need one per person.</li>
      <li>What does he actually do with the Funds tab each week? That decides what the firm's page shows first.</li>
      <li>How often is one meeting with several firms, like the Hartley lunch? I built one firm per meeting.</li>
    </ul>
  </div>
</div>
""", label="Questions")

# 15
slide("dark", """
<div class="eyebrow">Thanks</div>
<h2>Let's fix it<span class="accent">.</span></h2>
<p class="lead">Prototype: <span class="mono">crm / 4 - Corella CRM - Branch (reviewed).html</span><br>Note: <span class="mono">crm / 5 - Review and plan.html</span></p>
""", label="End")

# Appendix
slide("light", """
<div class="eyebrow">Appendix · for the 20 minutes with Jimmy</div>
<h2>One fix to suggest, and let Jimmy size it.</h2>
<div class="cols">
  <div class="card lift">
    <h3>Suggest this</h3>
    <p>The "who attended" box on a firm's log form is free text. Make it tick-boxes of the firm's people, and show the meeting on each person who was ticked.</p>
    <p class="muted">If it's quick, the meeting Josh logs on Larkspur appears on Priya, David and Tom: the pitch's test, passing in his branch. If it isn't quick, that's the answer to my first question.</p>
  </div>
  <div class="card">
    <h3>Not this</h3>
    <p>Rebuilding organisation as a proper record. That's the day 1 job, not a twenty-minute demo.</p>
    <h3 style="margin-top:20px">Then ask</h3>
    <p>"What would have to change underneath to make this real, and what else depends on it?" Then listen.</p>
  </div>
</div>
""", notes="For me, not the panel.", label="Live fix")

slide("light", """
<div class="eyebrow">Appendix · decisions</div>
<h2>Backup for questions.</h2>
<p class="muted">If someone asks "why did you do it that way", the answer is in here. Not for presenting.</p>
<table class="t small">
  <tr><th>Fork</th><th>Chose</th><th>Why</th></tr>
  <tr><td>Email vs pack</td><td>Email; plan folded in</td><td>Most recent instruction; covering both costs little</td></tr>
  <tr><td>New repo vs their file</td><td>Their file</td><td>No build step, their tokens, "zip the folder"</td></tr>
  <tr><td>Label vs record</td><td>Record</td><td>Every failure traces to the label</td></tr>
  <tr><td>Group-by vs list</td><td>Separate list, no tabs</td><td>A sub-tab is how the feature got missed</td></tr>
  <tr><td>Duplicates</td><td>Suggest all, auto-merge none</td><td>The pitch says don't guess</td></tr>
  <tr><td>Old spellings</td><td>Kept on the master</td><td>Data integrity; future imports land right</td></tr>
  <tr><td>Attendees</td><td>Picked from the firm's people</td><td>The test needs it on each person</td></tr>
  <tr><td>Choosing a firm</td><td>Searchable picker</td><td>Dropdowns blow out; typing made duplicates</td></tr>
  <tr><td>Confirmations</td><td>Inline</td><td>Browser dialogs can't say what's kept</td></tr>
  <tr><td>Summary per firm</td><td>Out</td><td>A canned one would be a fake</td></tr>
  <tr><td>Per-firm template</td><td>Built, then pulled</td><td>Belongs with the importer</td></tr>
  <tr><td>Permissions, importer</td><td>Out</td><td>Not in the pitch; next problem</td></tr>
</table>
""", label="Decisions")

# --------------------------------------------------------------------------
def render():
    sections = []
    for i, s in enumerate(SLIDES):
        notes = f'<div class="notes" role="note" aria-label="Speaker notes">{s["notes"]}</div>' if s["notes"] else ""
        sections.append(f'<section class="slide {s["kind"]}" id="s{i+1}" data-label="{s["label"]}" aria-label="Slide {i+1}: {s["label"]}"><div class="inner">{s["body"]}</div>{notes}</section>')
    n = len(SLIDES)
    toc = "".join(f'<a href="#s{i+1}"><span class="num">{i+1:02d}</span>{s["label"]}</a>' for i, s in enumerate(SLIDES))
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Organisations in the CRM · panel</title>
<style>
{fonts}
</style>
<style>
{tokens}
</style>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-snap-type:y mandatory;scroll-behavior:smooth}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
:focus-visible{{outline:3px solid var(--color-forest-light);outline-offset:3px}}
.dark :focus-visible,.on-dark :focus-visible,.overview :focus-visible{{outline-color:var(--color-neon)}}
.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}}
body{{background:var(--color-canvas);color:var(--color-text);font-family:var(--font-body);font-size:var(--text-body);line-height:var(--leading-body);-webkit-font-smoothing:antialiased;font-synthesis:none}}
a{{color:inherit;text-decoration:none}}
b,strong,h1,h2,h3{{font-weight:var(--font-weight-medium)}}
q{{quotes:"\\201C" "\\201D";font-style:italic}}

/* ---------- chrome ---------- */
.nav-wrap{{position:fixed;top:0;left:0;right:0;z-index:20;padding:var(--header-top) var(--gutter-header-mobile) 0;pointer-events:none}}
@media(min-width:1024px){{.nav-wrap{{padding-inline:var(--gutter-desktop)}}}}
.nav-pill{{display:flex;align-items:center;justify-content:space-between;height:var(--header-height);max-width:var(--max-width-site);margin-inline:auto;padding:0 12px 0 20px;border-radius:var(--radius-full);pointer-events:auto}}
.wordmark{{display:flex;align-items:center;gap:8px;font-size:22px;font-weight:var(--font-weight-medium);letter-spacing:-.01em}}
.wordmark .mark{{width:22px;height:22px;border-radius:6px;border:2px solid var(--color-forest-light);position:relative}}
.wordmark .mark::after{{content:"";position:absolute;inset:4px;border-top:2px solid var(--color-forest-light);border-right:2px solid var(--color-forest-light);transform:rotate(45deg) translate(-2px,2px)}}
.on-dark .wordmark .mark,.on-dark .wordmark .mark::after{{border-color:var(--color-neon)}}
.on-dark .wordmark{{color:#fff}}
.chrome-right{{display:flex;align-items:center;gap:10px;font-family:var(--font-mono);font-size:var(--text-xs);letter-spacing:.08em;text-transform:uppercase;color:var(--color-slate)}}
.on-dark .chrome-right{{color:rgb(var(--color-white-rgb)/.85)}}
.chrome-right a,.chrome-right button{{font:inherit;color:inherit;background:none;border:1px solid currentColor;border-radius:var(--radius-full);padding:6px 12px;cursor:pointer}}
.chrome-right a:hover,.chrome-right button:hover,.chrome-right button[aria-pressed=true]{{background:rgb(var(--color-forest-rgb)/.08)}}
.on-dark .chrome-right a:hover,.on-dark .chrome-right button:hover,.on-dark .chrome-right button[aria-pressed=true]{{background:rgb(var(--color-white-rgb)/.14)}}
.progress{{position:fixed;left:0;bottom:0;height:3px;background:var(--color-neon);z-index:21;width:0;transition:width var(--duration-base) var(--ease-default)}}

/* ---------- slides ---------- */
.slide{{min-height:100svh;scroll-snap-align:start;display:flex;align-items:center;position:relative;padding:calc(var(--header-top) + var(--header-height) + 24px) var(--gutter-mobile) 56px}}
@media(min-width:1024px){{.slide{{padding-inline:var(--gutter-desktop)}}}}
.inner{{width:100%;max-width:var(--max-width-site);margin-inline:auto}}
.slide.light{{background:var(--color-canvas)}}
.slide.light:nth-of-type(4n+1){{background:var(--color-sand)}}
.slide.dark{{background:var(--gradient-hero-home);color:var(--color-text-on-dark);isolation:isolate;overflow:hidden}}
.slide.dark::before{{content:"";position:absolute;inset:0;z-index:-1;background-image:linear-gradient(rgb(255 255 255/.027) 1px,transparent 1px),linear-gradient(90deg,rgb(255 255 255/.027) 1px,transparent 1px);background-size:72px 72px;-webkit-mask-image:radial-gradient(85% 75% at 50% 35%,#000 25%,transparent 100%);mask-image:radial-gradient(85% 75% at 50% 35%,#000 25%,transparent 100%)}}
.slide.dark::after{{content:"";position:absolute;z-index:-1;width:700px;height:700px;top:-25%;left:-12%;border-radius:50%;filter:blur(var(--blur-blob));opacity:.45;background:radial-gradient(circle at 30% 30%,rgb(0 255 180/.42),transparent 68%);pointer-events:none}}

.eyebrow{{font-family:var(--font-mono);font-size:var(--text-eyebrow);font-weight:var(--font-weight-medium);letter-spacing:var(--tracking-eyebrow);text-transform:uppercase;color:var(--color-forest);margin-bottom:14px}}
.dark .eyebrow{{color:rgb(var(--color-neon-rgb)/.85)}}
h1{{font-size:var(--text-display);line-height:var(--leading-display);letter-spacing:var(--tracking-display);max-width:var(--max-width-h1);text-wrap:balance}}
h2{{font-size:var(--text-h2);line-height:var(--leading-heading);letter-spacing:var(--tracking-display);max-width:900px;text-wrap:balance;margin-bottom:28px}}
h3{{font-size:var(--text-h3);line-height:var(--leading-tight);letter-spacing:var(--tracking-h3);margin-bottom:8px}}
h1 .accent,h2 .accent{{color:var(--color-neon)}}
.lead{{font-size:var(--text-lead);line-height:var(--leading-relaxed);max-width:var(--max-width-lead);color:var(--color-slate);margin-top:8px}}
.dark .lead{{color:var(--color-text-on-dark-lead)}}
.byline{{margin-top:40px;font-family:var(--font-mono);font-size:var(--text-caption);letter-spacing:.06em;color:rgb(var(--color-white-rgb)/.8)}}
p{{margin-bottom:12px;max-width:62ch}}
p.big{{font-size:var(--text-body-lg);line-height:var(--leading-relaxed)}}
p.quote{{font-size:var(--text-quote);line-height:1.5;max-width:900px;padding-left:20px;border-left:3px solid var(--color-neon);margin:16px 0 20px}}
.muted{{color:var(--color-slate);font-size:var(--text-body-sm)}}
.dark .muted{{color:rgb(var(--color-white-rgb)/.78)}}
.mono{{font-family:var(--font-mono);font-size:var(--text-caption)}}
ul,ol{{padding-left:22px;margin-bottom:12px}}
li{{margin-bottom:8px;max-width:62ch}}
ul.plain{{list-style:none;padding:0}}
ul.plain li{{padding:8px 0;border-bottom:1px solid var(--color-border-light)}}
ul.plain li:last-child{{border-bottom:0}}
ul.plain.small li{{font-size:var(--text-body-sm);padding:6px 0}}
ul.big-list li{{font-size:var(--text-lead);line-height:var(--leading-relaxed);margin-bottom:18px;max-width:60ch}}
ol.calls li,ol.days li{{margin-bottom:10px;max-width:none}}
ol.days{{list-style:none;padding:0}}
ol.days li{{display:grid;grid-template-columns:90px 1fr;gap:16px;padding:9px 0;margin:0;border-bottom:1px solid var(--color-border-light)}}
ol.days .d{{font-family:var(--font-mono);font-size:var(--text-caption);color:var(--color-forest);padding-top:3px}}

.cols{{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:start}}
.cols.wide{{grid-template-columns:1.35fr 1fr;align-items:center}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:var(--grid-gap)}}
.grid3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--grid-gap);margin-bottom:16px}}
@media(max-width:860px){{.cols,.cols.wide,.grid2,.grid3{{grid-template-columns:1fr}}}}

.card{{background:#fff;border-radius:var(--radius-panel);padding:var(--card-padding-sm);box-shadow:var(--ring-light)}}
.card p:last-child{{margin-bottom:0}}
.card.lift{{background:var(--parchment-accent);box-shadow:0 0 0 1px var(--color-positive-border)}}
.card.warn{{background:var(--color-warning-bg);box-shadow:0 0 0 1px var(--color-warning-border)}}
.card.glass{{background:var(--color-glass-card);box-shadow:var(--ring-dark);backdrop-filter:blur(var(--blur-card));color:rgb(var(--color-white-rgb)/.86)}}
.card.glass h3{{color:#fff}}
.card.glass.neon{{box-shadow:0 0 0 1px rgb(var(--color-neon-rgb)/.45),var(--shadow-glow)}}

.stats{{display:grid;gap:14px}}
.stat{{background:#fff;border-radius:var(--radius-panel);padding:18px 22px;box-shadow:var(--ring-light);display:grid;grid-template-columns:90px 1fr;gap:16px;align-items:center}}
.stat .n{{font-family:var(--font-mono);font-size:var(--text-stat-sm);letter-spacing:var(--tracking-stat);color:var(--color-forest);line-height:1}}
.stat .l{{font-size:var(--text-body-sm);color:var(--color-slate)}}

table.t{{width:100%;border-collapse:collapse;background:#fff;border-radius:var(--radius-panel);overflow:hidden;box-shadow:var(--ring-light);margin-bottom:16px}}
table.t th{{text-align:left;font-family:var(--font-mono);font-size:var(--text-eyebrow);letter-spacing:.08em;text-transform:uppercase;color:var(--color-slate);font-weight:var(--font-weight-medium);padding:12px 16px;background:var(--color-sand);border-bottom:1px solid var(--color-border-light)}}
table.t td{{padding:12px 16px;border-bottom:1px solid var(--color-border-light);vertical-align:top;font-size:var(--text-body-sm);line-height:1.5}}
table.t tr:last-child td{{border-bottom:0}}
table.t td:first-child{{width:34%;color:var(--color-text)}}
table.t.small td{{padding:7px 12px;font-size:var(--text-caption)}}
table.t.small td:first-child{{width:22%}}

.shot{{border-radius:var(--radius-xl);overflow:hidden;box-shadow:var(--shadow-feature),var(--ring-light);background:#fff;max-height:62svh}}
.shot img{{display:block;width:100%;height:auto;max-height:62svh;object-fit:cover;object-position:top}}
.cols.wide .shot + p, .cols.wide p + .shot{{margin-top:14px}}
.cols.wide > div > .shot{{max-height:34svh}}
.cols.wide > div > .shot img{{max-height:34svh;object-fit:contain;object-position:top left}}

/* ---------- voice ---------- */
.quotes blockquote{{margin:0 0 14px;padding:12px 18px;border-left:3px solid var(--color-neon);background:#fff;border-radius:0 var(--radius-card) var(--radius-card) 0;box-shadow:var(--ring-light);font-size:var(--text-body-lg);line-height:1.5;font-style:italic;max-width:60ch}}
.who{{display:grid;gap:10px}}
.who > div{{background:#fff;border-radius:var(--radius-panel);padding:12px 16px;box-shadow:var(--ring-light);font-size:var(--text-body-sm);line-height:1.5}}
.who .k{{display:block;font-family:var(--font-mono);font-size:var(--text-eyebrow);letter-spacing:.1em;text-transform:uppercase;color:var(--color-forest);margin-bottom:3px}}
.test{{margin-top:14px;padding:12px 16px;background:var(--parchment-accent);border-radius:var(--radius-card);box-shadow:0 0 0 1px var(--color-positive-border);max-width:none}}
ol.steps,ul.idea{{list-style:none;padding:0;counter-reset:n}}
ol.steps li,ul.idea li{{position:relative;padding:12px 0 12px 46px;border-bottom:1px solid var(--color-border-light);max-width:none;font-size:var(--text-body-lg);line-height:1.5}}
ol.steps li::before,ul.idea li::before{{counter-increment:n;content:counter(n);position:absolute;left:0;top:12px;width:30px;height:30px;border-radius:50%;background:var(--color-forest);color:#fff;font-family:var(--font-mono);font-size:13px;display:grid;place-items:center}}
table.t.rounds td{{font-size:var(--text-body-sm);line-height:1.5;padding:10px 16px}}
table.t.rounds td:first-child{{width:42%;font-style:italic;color:var(--color-forest)}}

/* ---------- notes ---------- */
.notes{{display:none;position:absolute;left:0;right:0;bottom:0;padding:14px var(--gutter-desktop);background:var(--color-ink);color:rgb(var(--color-white-rgb)/.88);font-size:var(--text-body-sm);border-top:2px solid var(--color-neon)}}
.notes::before{{content:"Notes · ";font-family:var(--font-mono);font-size:var(--text-eyebrow);letter-spacing:.1em;text-transform:uppercase;color:var(--color-neon)}}
body.show-notes .notes{{display:block}}

/* ---------- overview ---------- */
.overview{{display:none;position:fixed;inset:0;z-index:30;background:rgb(var(--color-ink-rgb)/.96);color:#fff;padding:80px var(--gutter-desktop) 40px;overflow:auto}}
body.show-overview .overview{{display:block}}
.overview .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;max-width:var(--max-width-site);margin-inline:auto}}
.overview a{{display:flex;gap:12px;align-items:baseline;padding:12px 14px;border-radius:var(--radius-card);background:rgb(255 255 255/.06);border:1px solid rgb(255 255 255/.08);font-size:var(--text-body-sm)}}
.overview a:hover{{background:rgb(255 255 255/.12)}}
.overview .num{{font-family:var(--font-mono);color:var(--color-neon);font-size:var(--text-xs)}}
.overview h2{{color:#fff;max-width:var(--max-width-site);margin-inline:auto;margin-bottom:20px;font-size:var(--text-h2-sm)}}
.overview .hint{{max-width:var(--max-width-site);margin:24px auto 0;color:rgb(var(--color-white-rgb)/.8);font-family:var(--font-mono);font-size:var(--text-xs);letter-spacing:.06em}}

@media print{{
  html{{scroll-snap-type:none}}
  .nav-wrap,.progress,.overview{{display:none}}
  .slide{{min-height:0;page-break-after:always;padding:24px}}
  .slide.dark{{background:var(--color-ink)!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .notes{{display:block;position:static;margin-top:16px}}
}}
</style>
</head>
<body>
<div class="nav-wrap" id="chrome">
  <nav class="nav-pill" aria-label="Deck controls">
    <a class="wordmark" href="index.html"><span class="mark" aria-hidden="true"></span>InvestorHub</a>
    <div class="chrome-right">
      <span id="counter" aria-live="polite">1 / {n}</span>
      <button type="button" id="btn-notes" aria-pressed="false" title="Toggle speaker notes (N)">Notes</button>
      <button type="button" id="btn-overview" aria-pressed="false" aria-controls="overview" title="All slides (O)">All slides</button>
      <a href="corella-crm-branch-reviewed.html" target="_blank" rel="noopener">Prototype ↗</a>
    </div>
  </nav>
</div>
<div class="progress" id="progress"></div>

<main id="deck">
{''.join(sections)}
</main>

<div class="overview" id="overview" role="dialog" aria-modal="true" aria-labelledby="overview-title">
  <h2 id="overview-title">All slides</h2>
  <div class="grid">{toc}</div>
  <div class="hint">Right arrow or space: next. Left arrow: back. N: notes. O: this view. Esc: close. The URL remembers where you are.</div>
</div>

<script>
(function () {{
  const slides = Array.from(document.querySelectorAll(".slide"));
  const n = slides.length;
  const counter = document.getElementById("counter");
  const progress = document.getElementById("progress");
  const chrome = document.getElementById("chrome");
  let current = 0;

  function go(i) {{
    i = Math.max(0, Math.min(n - 1, i));
    slides[i].scrollIntoView({{ behavior: "smooth", block: "start" }});
    history.replaceState(null, "", "#s" + (i + 1));
  }}
  function sync() {{
    const mid = window.innerHeight / 2;
    let best = 0, bestD = Infinity;
    slides.forEach(function (s, i) {{
      const r = s.getBoundingClientRect();
      const d = Math.abs(r.top + r.height / 2 - mid);
      if (d < bestD) {{ bestD = d; best = i; }}
    }});
    current = best;
    counter.textContent = (best + 1) + " / " + n;
    progress.style.width = ((best + 1) / n * 100) + "%";
    chrome.classList.toggle("on-dark", slides[best].classList.contains("dark"));
  }}
  window.addEventListener("scroll", sync, {{ passive: true }});
  window.addEventListener("resize", sync);
  document.addEventListener("keydown", function (e) {{
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
    const ov = document.body.classList.contains("show-overview");
    if (e.key === "Escape") {{ if (ov) setOverview(false); return; }}
    if (e.key === "o" || e.key === "O") {{ setOverview(!ov); return; }}
    if (e.key === "n" || e.key === "N") {{ setNotes(!document.body.classList.contains("show-notes")); return; }}
    if (ov) return;
    if (e.key === "ArrowRight" || e.key === "ArrowDown" || e.key === "PageDown" || e.key === " ") {{ e.preventDefault(); go(current + 1); }}
    else if (e.key === "ArrowLeft" || e.key === "ArrowUp" || e.key === "PageUp") {{ e.preventDefault(); go(current - 1); }}
    else if (e.key === "Home") {{ go(0); }}
    else if (e.key === "End") {{ go(n - 1); }}
  }});
  function setNotes(on) {{ document.body.classList.toggle("show-notes", on); document.getElementById("btn-notes").setAttribute("aria-pressed", String(on)); }}
  function setOverview(on) {{
    document.body.classList.toggle("show-overview", on);
    document.getElementById("btn-overview").setAttribute("aria-pressed", String(on));
    if (on) {{ const first = document.querySelector("#overview a"); if (first) first.focus(); }}
    else document.getElementById("btn-overview").focus();
  }}
  document.getElementById("btn-notes").addEventListener("click", function () {{ setNotes(!document.body.classList.contains("show-notes")); }});
  document.getElementById("btn-overview").addEventListener("click", function () {{ setOverview(!document.body.classList.contains("show-overview")); }});
  document.getElementById("overview").addEventListener("click", function (e) {{
    if (e.target.closest("a")) setOverview(false);
  }});
  // Land on the slide in the URL once fonts and images have settled, so nothing shifts under it.
  function landOnHash() {{
    const m = location.hash.match(/^#s(\\d+)$/);
    if (m) slides[Math.max(1, Math.min(n, parseInt(m[1], 10))) - 1].scrollIntoView({{ behavior: "instant", block: "start" }});
    sync();
  }}
  window.addEventListener("load", function () {{
    const ready = document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve();
    ready.then(function () {{ landOnHash(); setTimeout(landOnHash, 250); }});
  }});
  sync();
}})();
</script>
</body>
</html>
"""

out = ROOT / "preview" / "presentation.html"
out.write_text(render(), encoding="utf-8")
print("wrote", out, len(SLIDES), "slides")
