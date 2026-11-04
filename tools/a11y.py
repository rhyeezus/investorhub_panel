#!/usr/bin/env python3
"""Run axe-core (WCAG 2.1 A/AA) over the deck, the note and the prototype in
headless Chrome, including the prototype's dialogs and inline states.
Prints violations grouped by rule with the first few offending nodes.
Needs Playwright, a Chrome binary and /tmp/axe.min.js (npm pack axe-core)."""
import asyncio, os, json, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AXE = open("/tmp/axe.min.js", encoding="utf-8").read()
CHROME = os.environ.get("CHROME", "/usr/bin/google-chrome")
OPTS = {"runOnly": {"type": "tag", "values": ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "best-practice"]}}

async def audit(pg, label, results):
    await pg.add_script_tag(content=AXE)
    r = await pg.evaluate("(o) => axe.run(document, o)", OPTS)
    v = r["violations"]
    results.append((label, v))
    print(f"\n=== {label}: {len(v)} violation types")
    for x in v:
        print(f"  [{x['impact']}] {x['id']}: {x['help']}  ({len(x['nodes'])} nodes)")
        for n in x["nodes"][:3]:
            print("      -", n["target"][0][:110])

async def main():
    from playwright.async_api import async_playwright
    results = []
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1366, "height": 900})

        # Deck: a dark slide and a light slide, notes and overview open
        url = "file://" + os.path.join(ROOT, "preview", "presentation.html")
        await pg.goto(url + "#s1"); await pg.wait_for_timeout(600)
        await audit(pg, "deck (title slide)", results)
        await pg.goto(url + "#s7"); await pg.reload(); await pg.wait_for_timeout(600)
        await pg.keyboard.press("n"); await pg.wait_for_timeout(100)
        await audit(pg, "deck (table slide, notes shown)", results)
        await pg.keyboard.press("o"); await pg.wait_for_timeout(100)
        await audit(pg, "deck (overview open)", results)

        # Note
        await pg.goto("file://" + os.path.join(ROOT, "crm", "5 - Review and plan.html")); await pg.wait_for_timeout(400)
        await audit(pg, "note", results)

        # Prototype: contacts, contact page (edit), organisations (review open, bulk bar), org page (meeting form), picker, merge dialog, add contact
        crm = "file://" + os.path.join(ROOT, "crm", "4 - Corella CRM - Branch (reviewed).html")
        await pg.goto(crm + "#/contacts"); await pg.wait_for_timeout(400)
        await pg.evaluate("localStorage.clear()"); await pg.reload(); await pg.wait_for_timeout(400)
        await audit(pg, "prototype: contacts list", results)
        await pg.goto(crm + "#/contacts/c01"); await pg.wait_for_timeout(300)
        await pg.click("button[data-action=edit-details]"); await pg.wait_for_timeout(150)
        await audit(pg, "prototype: contact page, editing", results)
        await pg.goto(crm + "#/organisations"); await pg.wait_for_timeout(300)
        await pg.click("button[data-action=toggle-review]"); await pg.wait_for_timeout(150)
        for name in ["Corbett & Lane", "Corbett and Lane"]:
            await pg.locator("input.org-check[aria-label='Select " + name + "']").check()
        await pg.click("#bulk-bar button[data-action=confirm]"); await pg.wait_for_timeout(150)
        await audit(pg, "prototype: organisations, review open, bulk confirm", results)
        await pg.click("#bulk-bar button[data-action=cancel-confirm]"); await pg.wait_for_timeout(100)
        await pg.click("#bulk-bar button[data-action=merge-selected]"); await pg.wait_for_timeout(200)
        await audit(pg, "prototype: merge dialog", results)
        await pg.click("button[data-action=close-dialog]"); await pg.wait_for_timeout(100)
        await pg.click("button[data-action=add-org]"); await pg.wait_for_timeout(150)
        await pg.fill("#new-org-name", "lcm"); await pg.wait_for_timeout(100)
        await audit(pg, "prototype: new organisation dialog", results)
        await pg.click("button[data-action=close-dialog]"); await pg.wait_for_timeout(100)
        await pg.locator("tr.click", has_text="Larkspur Capital").first.locator("td.name-cell").click(); await pg.wait_for_timeout(300)
        await pg.click("button[data-action=focus-log]"); await pg.wait_for_timeout(200)
        await audit(pg, "prototype: organisation page, meeting form open", results)
        await pg.click("button[data-action=add-person]"); await pg.wait_for_timeout(200)
        await audit(pg, "prototype: add-people picker", results)
        await pg.click(".picker button[data-action=close-picker]"); await pg.wait_for_timeout(100)
        await pg.click("button[data-action=add-person]"); await pg.wait_for_timeout(150)
        await pg.fill("form[data-form=picker-create] input[name=name]", "Sam Test")
        await pg.click("form[data-form=picker-create] button[type=submit]"); await pg.wait_for_timeout(200)
        await audit(pg, "prototype: add contact dialog", results)
        await pg.goto(crm + "#/import"); await pg.wait_for_timeout(300)
        await audit(pg, "prototype: import", results)
        await b.close()

    total = sum(len(v) for _, v in results)
    print(f"\nTOTAL: {total} violation types across {len(results)} states")
    json.dump([(l, v) for l, v in results], open("/tmp/a11y.json", "w"))
    sys.exit(1 if total else 0)

asyncio.run(main())
