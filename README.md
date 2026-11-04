# InvestorHub · Product Builder panel · Organisations in the CRM

Homework for the panel on Thursday 5 November 2026. The task: review the engineer's week-1 build of "organisations" in the CRM, fix it, and bring a working prototype plus a one-page note.

## What's here

```
crm/
  1 - Read me first - Homework pack.pdf        the brief, as sent
  2 - Corella CRM - Today (before).html         the CRM before this work (InvestorHub's file, untouched)
  3 - Corella CRM - Branch (engineer's version).html   Jimmy's week-1 build (untouched)
  4 - Corella CRM - Branch (reviewed).html      the prototype: my version of the pitch, built on file 3
  5 - Review and plan.html                      the one-page note, in the CRM's design system; prints to PDF
docs/
  review-and-plan.md                            the note's text (edit this, then rebuild)
  review-and-plan.pdf                           printed copy
  screenshots/                                  the "done looks like" path, step by step
tools/
  build_note.py                                 markdown → crm/5 - Review and plan.html
  reassemble.py                                 src.stripped.html + the embedded fonts → crm/4
  src.stripped.html                             the prototype's source without the 170KB of base64 fonts
  test.py, test2.py                             drive the prototype in headless Chrome and screenshot it

DESIGNSYSTEM.md, src/styles/tokens.css,         InvestorHub's marketing-site design system, extracted from
tailwind.config.snippet.js, design-reference/   investorhub.com before the pack arrived. Not used by the
preview/index.html                              landing page: links to the prototype and the presentation
preview/presentation.html                       the panel talk-through as a slide deck (built by tools/build_deck.py)
preview/design-system.html                      the extracted style guide, rendered
preview/corella-crm-branch-reviewed.html        a copy of crm/4 for the preview links
  build_deck.py                                 slides (in the script) → preview/presentation.html
  a11y.py                                       axe-core audit of all three pages, incl. the prototype's dialogs
```

## The presentation

Open `preview/presentation.html`. Right arrow or space: next. Left arrow: back. **N** toggles speaker notes, **O** shows all slides, and the URL remembers where you are. Fifteen slides plus two appendix slides; the two prototype slides have screenshots as a fallback, but the plan is to switch to the live prototype for those.

Double-click any file in `crm/` to open it in Chrome. Each keeps its own demo data in the browser; "Reset demo data" at the bottom of any page starts again.

## The prototype in one minute

1. **Organisations** (new in the nav): 18 firms, with a review strip of 5 likely duplicates. Nothing merges until you click.
2. Merge the three Larkspurs, keeping "Larkspur Capital".
3. Open Larkspur Capital: Priya, David and Tom with their roles.
4. Log a meeting, ticking the three of them. It shows on the firm and on each person.

That's the pitch's "done looks like". The note explains the calls, what was left out, and what to ask Jimmy and Josh.

## Working on it

- Edit `tools/src.stripped.html`, then `python3 tools/reassemble.py "crm/4 - Corella CRM - Branch (reviewed).html"`.
- Edit `docs/review-and-plan.md`, then `python3 tools/build_note.py`.
- `python3 tools/test.py` and `test2.py` need Playwright and a Chrome binary; they print what they find at each step.
- `python3 tools/a11y.py` runs axe-core (WCAG 2.1 AA plus best practice) over the deck, the note and thirteen states of the prototype; it expects `/tmp/axe.min.js` from `npm pack axe-core`. Last run: zero violations.

All people, firms and figures are fictional, as in the pack.
