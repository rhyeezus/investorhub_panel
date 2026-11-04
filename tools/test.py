import asyncio, sys, os
from playwright.async_api import async_playwright

URL = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "crm", "4 - Corella CRM - Branch (reviewed).html"))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1366, "height": 900})
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.on("console", lambda m: errors.append("console." + m.type + ": " + m.text) if m.type in ("error",) else None)

        async def shot(name): await pg.screenshot(path=os.path.join(os.path.dirname(__file__), "..", "docs", "screenshots", f"{name}.png"), full_page=True)
        async def text(sel): return (await pg.locator(sel).first.inner_text()).strip()

        await pg.goto(URL + "#/organisations"); await pg.wait_for_timeout(300)
        print("H1:", await text("h1"))
        print("stats:", await text(".stats"))
        await pg.click("button[data-action=toggle-review]"); await pg.wait_for_timeout(200)
        review = pg.locator(".review-row")
        n = await review.count()
        print("review groups:", n)
        for i in range(n):
            print("  -", (await review.nth(i).locator(".review-names").inner_text()).replace("\n", " "))
        await shot("01-organisations-before")

        # Merge the Larkspur group: pick 'Larkspur Capital' as master
        row = review.filter(has_text="Larkspur").first
        sel = row.locator("select[name=masterId]")
        opts = await sel.locator("option").all_inner_texts()
        print("larkspur options:", opts)
        await sel.select_option(label=[o for o in opts if o.startswith("Larkspur Capital (")][0])
        await row.locator("button:has-text('Merge')").click(); await pg.wait_for_timeout(300)
        print("after merge, review groups:", await pg.locator(".review-row").count())
        await shot("02-organisations-after-merge")

        # Open Larkspur Capital
        await pg.locator("tr.click", has_text="Larkspur Capital").first.locator("td.name-cell").click(); await pg.wait_for_timeout(300)
        print("org page H1:", await text("h1"), "|", await text(".card-head .sub"))
        print("people:", (await text("aside .section")).replace("\n", " | "))
        await shot("03-larkspur-page")

        # Log the August roadshow once with Priya, David, Tom
        await pg.click(".card-head button[data-action=focus-log]"); await pg.wait_for_timeout(200)
        for name in ["Priya Raman", "David Okafor", "Tom Avery"]:
            await pg.locator("form[data-form=log-meeting] label.check", has_text=name).locator("input").check()
        await pg.fill("form[data-form=log-meeting] input[name=date]", "2026-08-18")
        await pg.fill("#log-text", "August roadshow: Priya keen on loan growth; David asked about late repayments. Send David the late-repayments data.")
        await pg.click("form[data-form=log-meeting] button[type=submit]"); await pg.wait_for_timeout(300)
        print("org timeline first row:", (await pg.locator(".main ul.rows li").first.inner_text()).replace("\n", " | "))
        await shot("04-larkspur-after-meeting")

        # Check each attendee's page
        for cid, name in [("c01", "Priya"), ("c02", "David"), ("c03", "Tom")]:
            await pg.goto(URL + "#/contacts/" + cid); await pg.wait_for_timeout(200)
            rows = await pg.locator(".main ul.rows li").all_inner_texts()
            hit = [r for r in rows if "August roadshow" in r]
            print(name, "sees meeting:", bool(hit), "| org link:", await text(".rail .kv"))
        await shot("05-priya-page")

        # Contact page: change Ella's organisation via the dropdown to Kestrel Point
        await pg.goto(URL + "#/contacts/c04"); await pg.wait_for_timeout(200)
        await pg.click("button[data-action=edit-details]"); await pg.wait_for_timeout(100)
        opts = await pg.locator("select[name=organisationId] option").all_inner_texts()
        print("org dropdown options:", opts)
        await pg.locator("select[name=organisationId]").select_option(label=[o for o in opts if o.startswith("Kestrel")][0])
        await pg.click("form[data-form=edit-details] button[type=submit]"); await pg.wait_for_timeout(200)
        print("Ella now:", await text(".rail .kv"))
        print("Ella timeline top:", (await pg.locator(".main ul.rows li").first.inner_text()).replace("\n", " | "))

        # Contacts list shows org links
        await pg.goto(URL + "#/contacts"); await pg.wait_for_timeout(200)
        print("contacts header:", await text("table.t thead"))
        await shot("06-contacts")

        # Not a firm: remove BHP
        await pg.goto(URL + "#/organisations"); await pg.wait_for_timeout(200)
        await pg.locator("tr.click", has_text="BHP").first.locator("td.name-cell").click(); await pg.wait_for_timeout(200)
        pg.once("dialog", lambda d: asyncio.ensure_future(d.accept()))
        await pg.click("button[data-action=not-a-firm]"); await pg.wait_for_timeout(300)
        print("orgs after removing BHP:", await text(".stats"))

        # Import the Corella sample still drops rows (expected, documented)
        await pg.goto(URL + "#/import"); await pg.wait_for_timeout(200)
        await pg.select_option("select[data-change=import-sample]", "conference"); await pg.wait_for_timeout(200)
        await pg.click("button[data-action=preview-import]"); await pg.wait_for_timeout(200)
        print("conference preview stats:", await text(".stats"))
        await pg.click("button[data-action=run-import]"); await pg.wait_for_timeout(300)
        await pg.goto(URL + "#/organisations"); await pg.wait_for_timeout(200)
        print("after import, review groups:", await pg.locator(".review-row").count())
        for i in range(await pg.locator(".review-row").count()):
            print("  -", (await pg.locator(".review-row").nth(i).locator(".review-names").inner_text()).replace("\n", " "))
        await shot("07-organisations-after-import")

        print("ERRORS:", errors if errors else "none")
        await b.close()

asyncio.run(main())
