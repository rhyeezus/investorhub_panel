# Organisations in the CRM — review and plan

## The problem

The CRM stores every investor as one person, but Josh works by firm: a fund manager is a team — a portfolio manager and a couple of analysts — and he meets, plans and reports by the team. So Corella's institutional investors live in a spreadsheet the CRM can't load, and what he actually asked for — "load it so we can run everything from there" — isn't possible.

It isn't only Corella. The deal waited on "can't group people by firm", two lost deals cite the same gap, and 38 clients carry an "institution" tag spelled 11 ways. This is the pattern, not one customer.

**Who's who.** Corella Finance is the customer. Josh (IR manager) and Hannah are the users. InvestorHub's customer success team sits between — they already write notes in Corella's CRM, and they'll be the ones running the clean-up for clients who won't. The firms themselves (Larkspur, Hartley) are the subject of the data, not users of it.

**Two problems, not one.** The pitch is right: the CRM needs a place for a firm. But Josh's spreadsheet is a second, bigger problem — the importer keys on email and his sheet has names; notes can't import; people and roles sit in one cell. Organisations has to exist first; the importer is next. This note is about the first.

## What's wrong with the week-1 build

One cause, several symptoms. Organisation was built as a label — the old company field, renamed — rather than a record people belong to. Because the firm doesn't exist as a thing, there's nothing to open, nothing to rename, and nothing for a meeting to attach to. So:

- 18 "organisations" for 9 firms, because every spelling is a separate label (Larkspur is three; Corbett, Kestrel, Meridian and Hartley are two each). BHP and "Self-employed" are organisations too.
- No organisations list and no organisation page. Clicking a firm filters the contacts table and leaves the company-wide stats on top.
- Roles aren't shown anywhere a team is shown.
- A meeting logged on a firm takes attendees as free text and never reaches the people. Logging the August roadshow doesn't show on Priya, David or Tom. If "LCM" is later corrected to "Larkspur Capital", anything logged under "LCM" is stranded.
- Assigning someone to a firm means opening the person, editing, and typing — which is how the duplicates got there.
- The clean-up is left to Josh, one person at a time (the branch's own banner says so).

Against the pitch's "done looks like", none of the three steps works yet.

## The bet, and what's most likely wrong

If a firm is a record, and the one-off clean-up suggests merges for a person to confirm, Josh will trust the CRM over his sheet. The thing most likely to be wrong looks cheap in the prototype and may not be in production: Exhibit L says an activity belongs to one contact, and "logged once, shown on three people" needs it to belong to a firm and several people. That's the first question for Jimmy, and it decides whether day 2–3 below is a day or a week.

## The calls I made

1. **Organisation is a record** — an id, a name, and the old spellings it absorbed. Everything else follows from this.
2. **The one-off migration suggests, a person confirms.** Every company string becomes a firm; likely duplicates are flagged (same name once filler words are ignored, or initials); someone with context — Josh, or CS on his behalf — merges each group with one click. Nothing auto-merges. Retail employers get "not a firm".
3. **Merged spellings are kept as aliases**, so a later import with "LCM" lands on Larkspur instead of making a fourth one.
4. **A meeting is logged once on the firm with attendees ticked**, and shows on the firm and on each person.
5. **Organisation on a contact is picked, not typed** — a searchable picker from the contact's page or straight from the contacts list, with "create new" as a separate, explicit step. The free-text box goes.
6. **Role reuses the occupation field**, relabelled. The data was already there.
7. **Each firm has its own import template**, with the company column pre-filled, so a file Josh sends for Larkspur lands on Larkspur.

## What I'd fix in the five days, in order

1. Make organisation a record and point contacts at it. Day 1 — everything depends on it.
2. The migration with the review screen, so the data is right before CS or Josh see it. Day 1–2.
3. The organisation page: people with roles, log a meeting with attendees, timeline. Day 2–3. This is the "done looks like" test.
4. Organisations list in the nav, with merge. Day 3.
5. Contact page: dropdown, role label, list links. Day 4.
6. Walk CS through it Thursday; fix what they find. Day 5.

## How we'd know it worked

Josh logs the February roadshow on firms instead of in the sheet; the Funds tab stops being updated; CS stop hearing "can't group by firm". Later, and countable: meetings logged on firms per client, and how many clients have run the review screen.

## What I left out, and why

- Importing Josh's spreadsheet — the second problem above. The prototype leaves the failing import visible on purpose.
- Organisation type (fund manager / broker / super), owner per firm, follow-ups with a done status, email audiences by firm, any permissions model, linking firms to the ownership report (the pitch's next bet).
- A written summary of everything with a firm. Worth doing once there's enough logged to summarise; a canned one in a prototype would be a fake.
- General UX of the CRM — filters, tag creation and taxonomy, table sorting, pagination, phone formats. Real, not this cycle.

## Questions for Jimmy

- Was the string a time call for week 1, or a view that a record wasn't needed? What does a record cost in the real schema?
- Is "logged once, shown on three people" a schema change in production, or a view?
- Across other clients, how dirty is the company field — does the review screen need to handle hundreds of groups or dozens?
- What happens to Today data on migration? The branch currently discards saved state.

## What I'd want to learn from Josh

- Does he have an email for everyone in the Funds tab? If not, import can't key on email and we need another way in.
- What he actually does with the Funds tab week to week — plan the roadshow, report to the board on % held, chase follow-ups. That decides what the firm page shows first.
- How often a meeting has more than one firm in it (the Hartley lunch, the conference). One firm per meeting may not be enough.
- Who else uses the sheet (Hannah), and whether "Ours" needs to be a field.
- Whether he needs the Old tab, or it's history he can leave behind.

## An assumption to flag

The pack asked for a one-page plan with no build; the email asked for a prototype and a note. I followed the email and folded the plan's three items into this note.
