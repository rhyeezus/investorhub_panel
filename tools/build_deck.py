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

slide("dark", """
<div class="eyebrow">Product Builder panel · 5 November 2026</div>
<h1>Organisations in the CRM<span class="accent">.</span></h1>
<p class="lead">A review of the week-1 build, what I'd fix in the five days left, and a working prototype of where it should land.</p>
<p class="byline">Rhys Gourley</p>
""", notes="Fifteen minutes. The shape: what the problem actually is, what Jimmy built against it, one diagnosis, the calls I made, the prototype, the fix order, what I left out, and the questions I need answered before Monday.", label="Title")

slide("light", """
<div class="eyebrow">The ask</div>
<h2>One week left in a two-week cycle.</h2>
<div class="cols">
  <div>
    <p>Rhys shaped the pitch. Jimmy picked it up and built week one. Before customer success sees it on Thursday, it's mine to review and fix.</p>
    <p>Two briefs arrived: the pack asked for a one-page plan and no build; the email asked for a working prototype and a note. I followed the email and folded the plan into the note.</p>
  </div>
  <div class="card">
    <div class="eyebrow">Today, in the room</div>
    <ul class="plain">
      <li><b>15 min</b> this review, with Jimmy and Rhys</li>
      <li><b>20 min</b> fix the branch with Jimmy</li>
      <li><b>20 min</b> walk customer success through it</li>
      <li><b>5 min</b> my questions</li>
    </ul>
  </div>
</div>
""", notes="Name the brief discrepancy once, lightly, and move on. It shows I read both and made a call.", label="The ask")

slide("light", """
<div class="eyebrow">The problem</div>
<h2>Josh works by firm. The CRM only knows people.</h2>
<div class="cols">
  <div>
    <p class="big">A fund manager is a team (a portfolio manager and a couple of analysts) and Josh meets, plans and reports by the team. So Corella's institutional investors live in a spreadsheet, and the CRM can't load it.</p>
    <p>What he actually asked for: <q>Here's our investor CRM. Can you load it into InvestorHub so we can run everything from there?</q></p>
  </div>
  <div class="stats">
    <div class="stat"><div class="n">27</div><div class="l">fund managers in Josh's sheet, each with its people and meetings</div></div>
    <div class="stat"><div class="n">11</div><div class="l">spellings of the "institution" tag across 38 clients</div></div>
    <div class="stat"><div class="n">2</div><div class="l">lost deals citing "can't hold a fund and its people"</div></div>
  </div>
</div>
""", notes="This is the pattern, not one customer. The deal waited on it; lost deals cite it; 38 clients have hacked around it with tags.", label="Problem")

slide("light", """
<div class="eyebrow">Who's who</div>
<h2>Customer, users, and the people in between.</h2>
<div class="grid3">
  <div class="card"><div class="eyebrow">Customer</div><h3>Corella Finance</h3><p>Pays for the CRM. The sales deal was waiting on this.</p></div>
  <div class="card"><div class="eyebrow">Users</div><h3>Josh and Hannah</h3><p>Investor relations. They feel the pain every roadshow, and they're the ones who'll stop using the spreadsheet, or won't.</p></div>
  <div class="card"><div class="eyebrow">In between</div><h3>Customer success</h3><p>Already writing notes in Corella's CRM. They'll run the clean-up for clients who won't do it themselves.</p></div>
</div>
<p class="muted">The firms, Larkspur and Hartley, are the subject of the data, not users of it.</p>
""", notes="Two-sided business: the panel will listen for whether I collapse customer and user into one. I don't.", label="Who's who")

slide("light", """
<div class="eyebrow">Framing</div>
<h2>Two problems, not one.</h2>
<div class="cols">
  <div class="card lift">
    <div class="eyebrow">This cycle</div>
    <h3>The CRM needs a place for a firm.</h3>
    <p>The pitch is right. A record for a firm that people belong to, with its meetings in one place. This is what the five days are for.</p>
  </div>
  <div class="card">
    <div class="eyebrow">Next</div>
    <h3>Josh's spreadsheet still can't be loaded.</h3>
    <p>The importer keys on email and his sheet has names. Notes can't import. People and roles sit in one cell. Bigger than organisations, and it needs organisations to exist first.</p>
  </div>
</div>
""", notes="Separating these is the most important framing move. Jimmy's branch leaves the Corella sample import dropping every row, and so does my prototype, on purpose.", label="Two problems")

slide("light", """
<div class="eyebrow">The pitch's own test</div>
<h2>"Done looks like"</h2>
<p class="big quote">Josh at Corella opens Larkspur Capital, sees Priya, David and Tom with their roles, and logs the August roadshow meeting once.</p>
<p>Three steps. Everything that follows is measured against them.</p>
""", notes="Read it out. Everything in the review is 'does this step work yet'.", label="Done looks like")

slide("light", """
<div class="eyebrow">The week-1 build</div>
<h2>Against the pitch's five parts</h2>
<table class="t">
  <tr><th>Pitch</th><th>Branch</th></tr>
  <tr><td>Organisations list: every firm with its people</td><td>Not built. A "group by organisation" checkbox on Contacts. <b>18 groups for 9 firms.</b></td></tr>
  <tr><td>Organisation page: people, roles, everything that's happened</td><td>Not a page. The contacts table filtered to one string, company-wide stats still on top, no roles.</td></tr>
  <tr><td>Log a meeting once</td><td>Partly. Attendees as free text, stored against the name string. <b>Never reaches Priya, David or Tom.</b></td></tr>
  <tr><td>Organisation on a contact, changeable</td><td>A renamed free-text box with suggestions. New spellings still get typed.</td></tr>
  <tr><td>Start with what's there</td><td>Company field copied verbatim. No review, no merge. "Seeing a firm twice? Open each person."</td></tr>
</table>
<p class="muted">Kept from week 1: the audit line when a person's firm changes, and the import mapping the company column.</p>
""", notes="Facts only here; the diagnosis is the next slide. Credit what Jimmy did well: the org_change audit trail is a good instinct and it survives into my version.", label="Week-1 build")

slide("dark", """
<div class="eyebrow">Diagnosis</div>
<h2>One cause, several symptoms.</h2>
<div class="cols">
  <div class="card glass">
    <div class="eyebrow">What was built</div>
    <h3>A label</h3>
    <p>The firm is words typed on each person. "Larkspur Capital" on Priya, "Larkspur Capital Mgmt" on David, "LCM" on Tom. Nothing to open, nothing to rename, nothing for a meeting to attach to.</p>
  </div>
  <div class="card glass neon">
    <div class="eyebrow">What the pitch asked for</div>
    <h3>A record</h3>
    <p>The firm exists once, like a contact does. People point at it. Rename it and everyone follows. Log a meeting on it and it stays with it.</p>
  </div>
</div>
<p class="lead">Every visible problem traces back to this one choice. Fix it and the rest is assembly.</p>
""", notes="Sticky note on each person versus a folder you put people in. This is the sentence for Jimmy: not 'the UI is wrong', but 'the model is a label and the pitch needs a record'.", label="Diagnosis")

slide("light", """
<div class="eyebrow">The bet</div>
<h2>If a firm is a record, and the clean-up suggests merges for a person to confirm, Josh will trust the CRM over his sheet.</h2>
<div class="cols">
  <div class="card warn">
    <div class="eyebrow">Most likely to be wrong</div>
    <p>It looks cheap in the prototype and may not be in production. Exhibit L says an activity belongs to <b>one</b> contact. "Logged once, shown on three people" needs it to belong to a firm and several people.</p>
    <p><b>First question for Jimmy.</b> It decides whether days 2–3 are a day or a week.</p>
  </div>
  <div>
    <div class="eyebrow">Assumptions I'm carrying</div>
    <ul>
      <li>CS will run the clean-up for clients who won't.</li>
      <li>A firm is the right unit this cycle; funds within a firm are the next bet, as the pitch says.</li>
      <li>Suggesting duplicates by name is enough; the pitch rules out guessing from email domains, and I didn't.</li>
    </ul>
  </div>
</div>
""", notes="Say the riskiest assumption out loud before anyone asks. It's the thing I can't verify from a mock.", label="The bet")

slide("light", """
<div class="eyebrow">The calls I made</div>
<h2>Seven decisions, one of them doing most of the work.</h2>
<ol class="calls">
  <li><b>Organisation is a record</b>: id, name, and the spellings it absorbed.</li>
  <li><b>The migration suggests, a person confirms.</b> Every company string becomes a firm; likely duplicates are flagged by name or initials; Josh or CS merges each with one click. Nothing auto-merges.</li>
  <li><b>Merged spellings become aliases</b>, so a later import with "LCM" lands on Larkspur.</li>
  <li><b>A meeting is logged once on the firm, attendees ticked</b>, and shows on the firm and on each person.</li>
  <li><b>Organisation on a contact is picked, not typed</b>: a searchable picker, with "create new" an explicit step.</li>
  <li><b>Role reuses the occupation field</b>, relabelled. The data was already there.</li>
  <li><b>Creating a firm runs straight into adding its people</b>, and warns on a duplicate name.</li>
</ol>
""", notes="One and two are the product calls. Three to seven follow from them.", label="The calls")

slide("dark", """
<div class="eyebrow">The prototype</div>
<h2>Built in the branch file, on their design system.</h2>
<p class="lead">Plain JavaScript, one file, double-click to open. The same tokens and fonts as the product. Everything that follows is clickable.</p>
<p class="muted">crm / 4 - Corella CRM - Branch (reviewed).html</p>
""", notes="Switch to the prototype tab now and walk the next eight slides live. The screenshots are the fallback.", label="Prototype")

slide("light", """
<div class="eyebrow">1 · Organisations</div>
<h2>A list of firms, and a review of what the old field left behind.</h2>
<div class="cols wide">
  """ + img("r2-01-orgs-collapsed.png", "Organisations list with the review notice collapsed") + """
  <div>
    <p>New in the nav. Eighteen firms on first load, straight from the company field, and a notice: <b>five likely duplicates</b>. Nothing is merged until someone says so.</p>
    <p>Larkspur as three. Corbett, Kestrel, Meridian and Hartley as two each. BHP and "Self-employed" in the list, because the field held employers too.</p>
  </div>
</div>
""", label="Walk 1")

slide("light", """
<div class="eyebrow">2 · Merge</div>
<h2>Pick the name to keep. Everyone and everything moves across.</h2>
<div class="cols wide">
  """ + img("r4-merge-dialog.png", "Merge dialog: which name do we keep?") + """
  <div>
    <p>From the review row or from ticking rows in the list. One dialog either way: <b>which name do we keep?</b></p>
    <p>The other spellings become "also known as", so the next CSV with "LCM" in it lands on Larkspur instead of making a fourth.</p>
    <p>"Different firms" dismisses a suggestion. Retail employers get "Remove organisation": the people stay, the label goes.</p>
  </div>
</div>
""", label="Walk 2")

slide("light", """
<div class="eyebrow">3 · The firm</div>
<h2>Larkspur Capital: the team, with roles, and everything that's happened.</h2>
<div class="cols wide">
  """ + img("r3-org-page.png", "Larkspur Capital organisation page") + """
  <div>
    <p>Priya, David, Tom and Ella, with the roles Josh's sheet already had. A timeline of meetings, notes and calls with the firm or any of its people. No bulk-email noise.</p>
    <p><b>Add people</b> opens a searchable picker that stays open until you're done: an existing contact, or someone new with the firm already filled in.</p>
  </div>
</div>
""", label="Walk 3")

slide("light", """
<div class="eyebrow">4 · Log it once</div>
<h2>Tick who was there. It shows on the firm and on each of them.</h2>
<div class="cols wide">
  """ + img("05-priya-page.png", "Priya Raman's contact page showing the meeting logged on Larkspur") + """
  <div>
    <p>Log the August roadshow on Larkspur with Priya, David and Tom ticked. Open Priya: it's on her timeline: <i>With Larkspur Capital: David Okafor, Priya Raman, Tom Avery</i>.</p>
    <p class="big">That's the pitch's test, passing.</p>
  </div>
</div>
""", notes="This is the slide the whole review has been building to. Pause on it.", label="Walk 4")

slide("light", """
<div class="eyebrow">5 · Picked, not typed</div>
<h2>No more new spellings by accident.</h2>
<div class="cols wide">
  """ + img("r3-contacts.png", "Contacts list with Add to organisation on each row") + """
  <div>
    <p>On a person, and straight from the contacts list: <b>Add to organisation</b> opens the picker. Searching, not scrolling. "Create a new organisation" is its own step, and nothing is created until you save.</p>
    <p>New organisation checks the name as you type: <i>Larkspur Capital already exists (that's one of its other spellings)</i>, or <i>looks like it could be Bluegum Partners</i>.</p>
  </div>
</div>
""", label="Walk 5")

slide("light", """
<div class="eyebrow">The five days</div>
<h2>In order, because each one needs the last.</h2>
<ol class="days">
  <li><span class="d">Day 1</span><span><b>Organisation as a record; contacts point at it.</b> Everything depends on it.</span></li>
  <li><span class="d">Day 1–2</span><span><b>The migration with the review screen</b>, so the data is right before CS or Josh see it.</span></li>
  <li><span class="d">Day 2–3</span><span><b>The organisation page</b>: people with roles, log a meeting with attendees, timeline. The "done looks like" test.</span></li>
  <li><span class="d">Day 3</span><span><b>Organisations list in the nav, with merge.</b></span></li>
  <li><span class="d">Day 4</span><span><b>Contact page</b>: picker, role label, list links.</span></li>
  <li><span class="d">Day 5</span><span><b>Walk CS through it; fix what they find.</b></span></li>
</ol>
""", notes="If the schema answer from Jimmy is bad, day 2–3 stretches and days 4–5 compress. Say that.", label="Five days")

slide("light", """
<div class="eyebrow">What I left out, and why</div>
<h2>Thinness is a feature.</h2>
<div class="grid2">
  <div class="card"><h3>Josh's spreadsheet</h3><p>The second problem. The failing import is left visible on purpose. A per-firm import template waits for it.</p></div>
  <div class="card"><h3>The pitch's own "not this cycle"</h3><p>Linking firms to the ownership report, reporting per firm, firms shared across clients.</p></div>
  <div class="card"><h3>Nice, not now</h3><p>Organisation type, owner per firm, follow-ups with a done status, email audiences by firm, permissions.</p></div>
  <div class="card"><h3>A written summary per firm</h3><p>Worth doing once there's enough logged to summarise. A canned one in a prototype would be a fake.</p></div>
  <div class="card"><h3>General CRM UX</h3><p>Filters, tag creation and taxonomy, sorting, pagination. Real, not this cycle.</p></div>
</div>
""", notes="Being explicit about what's not built reads as discipline, not as gaps.", label="Left out")

slide("light", """
<div class="eyebrow">How we'd know</div>
<h2>Signals first, numbers later.</h2>
<div class="cols">
  <div>
    <ul>
      <li>Josh logs the February roadshow on firms, not in the sheet.</li>
      <li>The Funds tab stops being updated.</li>
      <li>CS stop hearing "can't group by firm".</li>
    </ul>
    <p class="muted">Countable later: meetings logged on firms per client; clients who've run the review screen.</p>
  </div>
  <div class="card">
    <div class="eyebrow">Rollout</div>
    <p>Corella first, with CS running the review screen. If it produces wrong merges, stop before the next client.</p>
  </div>
</div>
""", label="How we'd know")

slide("light", """
<div class="eyebrow">Questions</div>
<h2>What I need answered before Monday.</h2>
<div class="cols">
  <div>
    <div class="eyebrow">For Jimmy</div>
    <ul>
      <li>Was the string a time call for week 1, or a view that a record wasn't needed? What does a record cost in the real schema?</li>
      <li>Is "logged once, shown on three people" a schema change in production, or a view?</li>
      <li>Across other clients, how dirty is the company field: hundreds of duplicate groups, or dozens?</li>
    </ul>
  </div>
  <div>
    <div class="eyebrow">For customer success, on Josh's behalf</div>
    <ul>
      <li>Does he have an email for everyone in the Funds tab? If not, import can't key on email.</li>
      <li>What does he do with the Funds tab week to week: roadshows, % held, follow-ups? It decides what the firm page shows first.</li>
      <li>How often does a meeting have more than one firm in it, like the Hartley lunch or the conference?</li>
      <li>Who runs the clean-up for clients who won't?</li>
    </ul>
  </div>
</div>
""", label="Questions")

slide("dark", """
<div class="eyebrow">The 20 minutes with Jimmy</div>
<h2>One fix that proves the point, in his branch.</h2>
<div class="cols">
  <div class="card glass neon">
    <h3>Do this</h3>
    <p>On the org log form, replace the free-text attendees with checkboxes from the org's members, store their ids on the activity, and make each person's timeline include activities where they're an attendee.</p>
    <p class="muted">About twenty lines. Turns "logged once, invisible to Priya" into "logged once, on all three": the done-looks-like failure, fixed live.</p>
  </div>
  <div class="card glass">
    <h3>Don't do this</h3>
    <p>The record refactor. It's day 1 of the plan, not twenty minutes on someone else's laptop.</p>
    <h3 style="margin-top:20px">Then ask</h3>
    <p>"What would this cost in the real schema?" Then listen.</p>
  </div>
</div>
""", notes="This is for me, not the panel. Have it ready so the live session has a target.", label="Live fix")

slide("light", """
<div class="eyebrow">Five minutes · my questions for them</div>
<h2>Two things I'd want to know.</h2>
<ul class="big-list">
  <li>How far is the real schema from one-activity-one-contact: is a firm with several people on a meeting a migration, or a view?</li>
  <li>The next bet is linking firms to the ownership report. What does that need from organisations that I should be building towards now?</li>
</ul>
""", label="My questions")

slide("light", """
<div class="eyebrow">Appendix</div>
<h2>Decisions log</h2>
<table class="t small">
  <tr><th>Fork</th><th>Chose</th><th>Why</th></tr>
  <tr><td>Email vs pack</td><td>Email; plan folded in</td><td>Most recent instruction; covering both costs little</td></tr>
  <tr><td>New repo vs their file</td><td>Their file</td><td>No build step, their tokens embedded, "zip the folder"</td></tr>
  <tr><td>Review scope</td><td>Jimmy's work against the pitch</td><td>That's the brief; general UX to left-out</td></tr>
  <tr><td>Label vs record</td><td>Record</td><td>Every failure traces to the label</td></tr>
  <tr><td>Group-by vs list</td><td>Separate list; drop the checkbox; no tabs</td><td>A sub-tab is how Jimmy's feature got missed</td></tr>
  <tr><td>Duplicates</td><td>Suggest all, auto-merge none, human confirms</td><td>Pitch says don't guess; LCM is only Larkspur if someone knows</td></tr>
  <tr><td>Old spellings</td><td>Aliases on the master</td><td>Audit trail without clutter; future imports land right</td></tr>
  <tr><td>Attendees</td><td>Picked from the firm's people</td><td>"Done looks like" needs it on each person</td></tr>
  <tr><td>Org timeline</td><td>No bulk-email rows</td><td>Three campaigns × members swamps it</td></tr>
  <tr><td>Role</td><td>Reuse occupation</td><td>Data already there</td></tr>
  <tr><td>Choosing a firm</td><td>One searchable picker, both jobs</td><td>Dropdowns blow out; typing made duplicates</td></tr>
  <tr><td>Merge UI</td><td>Dialog with radios</td><td>One pattern for both paths</td></tr>
  <tr><td>Confirmations</td><td>Inline, spelling out what's kept and lost</td><td>Browser dialogs can't</td></tr>
  <tr><td>Per-firm template</td><td>Built, then pulled</td><td>Belongs with the importer; hard to explain in a sentence</td></tr>
  <tr><td>Summary per firm</td><td>Out</td><td>A canned one would be a fake</td></tr>
  <tr><td>Permissions, importer</td><td>Out</td><td>Not in the pitch; next problem</td></tr>
</table>
""", label="Decisions")

slide("light", """
<div class="eyebrow">Appendix</div>
<h2>Given · assumed · unknown</h2>
<div class="grid3">
  <div class="card"><div class="eyebrow">Given</div><ul class="plain small">
    <li>The pitch, its evidence, rabbit holes and not-this-cycle list</li>
    <li>Exhibit L: one activity, one contact; email is the key</li>
    <li>Josh's sheet: 27 firms, people and roles in one cell, meetings per tab</li>
    <li>The branch diff: ~180 lines, organisation as a string</li>
  </ul></div>
  <div class="card"><div class="eyebrow">Assumed</div><ul class="plain small">
    <li>Email supersedes the pack</li>
    <li>CS will run the clean-up</li>
    <li>Firm is the unit; funds next</li>
    <li>Name-based duplicate suggestions are enough</li>
  </ul></div>
  <div class="card"><div class="eyebrow">Unknown</div><ul class="plain small">
    <li>Cost of a record and of multi-person activities in the real schema</li>
    <li>How dirty the company field is across clients</li>
    <li>Whether Josh has emails for everyone</li>
    <li>What Josh does with the sheet week to week</li>
    <li>Whether Jimmy's week-1 call was discussed with Rhys</li>
  </ul></div>
</div>
""", label="Assumptions")

slide("dark", """
<div class="eyebrow">Thanks</div>
<h2>Let's fix it<span class="accent">.</span></h2>
<p class="lead">Prototype: <span class="mono">crm / 4 - Corella CRM - Branch (reviewed).html</span><br>Note: <span class="mono">crm / 5 - Review and plan.html</span></p>
""", label="End")

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

.shot{{border-radius:var(--radius-xl);overflow:hidden;box-shadow:var(--shadow-feature),var(--ring-light);background:#fff;max-height:66svh}}
.shot img{{display:block;width:100%;height:auto;max-height:66svh;object-fit:cover;object-position:top}}

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
