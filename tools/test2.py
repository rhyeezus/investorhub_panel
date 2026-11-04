import asyncio, os
from playwright.async_api import async_playwright
URL = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "crm", "4 - Corella CRM - Branch (reviewed).html"))
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1366, "height": 900})
        errors = []
        pg.on("pageerror", lambda e: errors.append(str(e)))
        pg.on("console", lambda m: errors.append("console.error: " + m.text) if m.type == "error" else None)
        async def shot(n): await pg.screenshot(path=os.path.join(os.path.dirname(__file__), "..", "docs", "screenshots", f"{n}.png"), full_page=True)
        async def text(sel): return (await pg.locator(sel).first.inner_text()).strip()

        # Organisations: review collapsed, then open
        await pg.goto(URL + "#/organisations"); await pg.wait_for_timeout(300)
        print("notice:", (await text(".notice")).replace("\n", " | "))
        print("review rows while collapsed:", await pg.locator(".review-row").count())
        await shot("r2-01-orgs-collapsed")
        await pg.click("button[data-action=toggle-review]"); await pg.wait_for_timeout(200)
        print("review rows open:", await pg.locator(".review-row").count())
        await shot("r2-02-orgs-review-open")
        lark = pg.locator(".review-row").filter(has_text="Larkspur").first
        opts = await lark.locator("select[name=masterId] option").all_inner_texts()
        await lark.locator("select[name=masterId]").select_option(label=[o for o in opts if o.startswith("Larkspur Capital (")][0])
        await lark.locator("button:has-text('Merge')").click(); await pg.wait_for_timeout(300)
        print("after Larkspur merge, review rows:", await pg.locator(".review-row").count())

        # Bulk bar: tick Meridian Lane + Meridian Lane AM → bar appears → Merge
        for name in ["Meridian Lane AM", "Meridian Lane"]:
            row = pg.locator("tr.click", has_text=name).first
            await row.locator("input.org-check").check()
        print("bulk bar:", (await text("#bulk-bar")).replace("\n", " | "), "| visible:", await pg.locator("#bulk-bar.on").count())
        await shot("r2-03-bulk-bar")
        await pg.click("#bulk-bar button[data-action=merge-selected]"); await pg.wait_for_timeout(200)
        await pg.locator("form[data-form=merge-dialog] select").select_option(label="Meridian Lane AM (2 people)")
        await pg.click("form[data-form=merge-dialog] button[type=submit]"); await pg.wait_for_timeout(300)
        print("after bulk merge, orgs stat:", (await text(".stat")).replace("\n", " "))

        # Org page: meeting form collapsed → Log meeting opens it → log → collapses
        await pg.locator("tr.click", has_text="Larkspur Capital").first.locator("td.name-cell").click(); await pg.wait_for_timeout(300)
        print("meeting form present while collapsed:", await pg.locator("form[data-form=log-meeting]").count())
        await shot("r2-04-larkspur-collapsed")
        await pg.click(".card-head button[data-action=focus-log]"); await pg.wait_for_timeout(200)
        print("meeting form after click:", await pg.locator("form[data-form=log-meeting]").count())
        for name in ["Priya Raman", "Tom Avery"]:
            await pg.locator("form[data-form=log-meeting] label.check", has_text=name).locator("input").check()
        await pg.fill("#log-text", "Quick call about the raise.")
        await pg.click("form[data-form=log-meeting] button[type=submit]"); await pg.wait_for_timeout(300)
        print("form collapsed again:", await pg.locator("form[data-form=log-meeting]").count() == 0)

        # Add a person via picker: search + pick existing
        await pg.click(".card-head button[data-action=add-person]"); await pg.wait_for_timeout(200)
        print("picker title:", await text(".picker h2"), "| items:", await pg.locator(".picker-item").count())
        await pg.fill("#picker-search", "grace"); await pg.wait_for_timeout(100)
        print("after search 'grace':", await pg.locator(".picker-item").count(), "|", (await text(".picker-item")).replace("\n", " · "))
        await shot("r2-05-picker-add-person")
        await pg.click(".picker-item"); await pg.wait_for_timeout(300)
        print("people now:", (await text("aside .section")).replace("\n", " | ")[:160])

        # Add someone new from the picker
        await pg.click(".card-head button[data-action=add-person]"); await pg.wait_for_timeout(200)
        await pg.fill("form[data-form=picker-create] input[name=name]", "Hannah Blake")
        await pg.click("form[data-form=picker-create] button[type=submit]"); await pg.wait_for_timeout(200)
        print("add-contact dialog open:", await pg.locator("form[data-form=add-contact]").count(), "| title:", await text("form[data-form=add-contact] h2"),
              "| first:", await pg.input_value("form[data-form=add-contact] [name=firstName]"), "| org field:", await text("form[data-form=add-contact] .org-field-name"))
        await shot("r2-06-add-new-prefilled")
        await pg.fill("form[data-form=add-contact] [name=email]", "hannah.blake@larkspurcapital.example")
        await pg.fill("form[data-form=add-contact] [name=occupation]", "Analyst")
        await pg.click("form[data-form=add-contact] button[type=submit]"); await pg.wait_for_timeout(300)
        print("stayed on org page:", "organisations" in pg.url, "| people count:", await text("aside .eyebrow"))

        # Contact edit: org field → picker → Create new (deferred until save)
        await pg.goto(URL + "#/contacts/c29"); await pg.wait_for_timeout(200)   # Aisha Rahman
        await pg.click("button[data-action=edit-details]"); await pg.wait_for_timeout(100)
        await pg.click("form[data-form=edit-details] button[data-action=pick-org]"); await pg.wait_for_timeout(200)
        await pg.fill("form[data-form=picker-create] input[name=name]", "Test Org")
        await pg.click("form[data-form=picker-create] button[type=submit]"); await pg.wait_for_timeout(200)
        print("field shows:", (await text("form[data-form=edit-details] .org-field-name")).replace("\n", " "), "| orgs before save:", await pg.evaluate("JSON.parse(localStorage.getItem('corella-crm-branch-organisations-reviewed')).organisations.length"))
        await shot("r2-07-edit-new-org-pending")
        await pg.click("form[data-form=edit-details] button[type=submit]"); await pg.wait_for_timeout(300)
        print("Aisha org after save:", (await text(".rail .kv")).split("Organisation")[1].split("Role")[0].strip().replace("\n", " "), "| orgs after save:", await pg.evaluate("JSON.parse(localStorage.getItem('corella-crm-branch-organisations-reviewed')).organisations.length"))

        # Contacts list row action
        await pg.goto(URL + "#/contacts"); await pg.wait_for_timeout(200)
        row = pg.locator("tr.click", has_text="Sophie Bennett").first
        await row.locator("button[data-action=pick-org-row]").click(); await pg.wait_for_timeout(200)
        await pg.fill("#picker-search", "bluegum"); await pg.wait_for_timeout(100)
        await pg.click(".picker-item"); await pg.wait_for_timeout(300)
        print("Sophie row:", (await pg.locator("tr.click", has_text="Sophie Bennett").first.inner_text()).replace("\n", " | ")[:80])
        await shot("r2-08-contacts-row-action")

        # Not a firm via bulk bar: BHP + Self-employed
        await pg.goto(URL + "#/organisations"); await pg.wait_for_timeout(200)
        for name in ["BHP", "Self-employed"]:
            await pg.locator("tr.click", has_text=name).first.locator("input.org-check").check()
        pg.once("dialog", lambda d: asyncio.ensure_future(d.accept()))
        await pg.click("#bulk-bar button[data-action=not-a-firm-selected]"); await pg.wait_for_timeout(300)
        print("orgs after bulk not-a-firm:", (await text(".stat")).replace("\n", " "))

        # Rename caution text present
        await pg.locator("tr.click", has_text="Larkspur Capital").first.locator("td.name-cell").click(); await pg.wait_for_timeout(200)
        await pg.click("button[data-action=edit-org]"); await pg.wait_for_timeout(100)
        print("rename help:", await text("form[data-form=edit-org] .help"))
        print("template link:", await pg.locator("button[data-action=download-org-template]").count())

        print("ERRORS:", errors if errors else "none")
        await b.close()
asyncio.run(main())
