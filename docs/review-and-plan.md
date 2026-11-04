# Organisations in the CRM: review and plan

## The problem

The CRM stores every investor as one person, but Josh works by firm: a fund manager is a team, and he meets, plans and reports by the team. So Corella's institutional investors live in a spreadsheet the CRM can't load, and what he asked for, "load it so we can run everything from there", isn't possible.

It isn't only Corella. The deal waited on "can't group people by firm", two lost deals cite the same gap, and 38 clients carry an "institution" tag spelled 11 ways. This is the pattern, not one customer.

**Who's who.** Corella is the customer; Josh and Hannah the users; customer success sits between, already writing notes in Corella's CRM. The firms are the subject of the data, not users of it.

**Two problems, not one.** The pitch is right: the CRM needs a place for a firm. Josh's spreadsheet is a second, bigger problem: the importer keys on email and his sheet has names; notes can't import. Organisations first; the importer next. This note is about the first.

## What's wrong with the week-1 build

One cause, several symptoms. Organisation was built as a label (the old company field, renamed), not a record people belong to. The firm doesn't exist as a thing, so there's nothing to open, rename, or attach a meeting to:

- 18 "organisations" for 9 firms: every spelling is its own label (Larkspur is three). BHP and "Self-employed" are organisations too.
- No organisations list or page: a firm is a filtered contacts table with the company-wide stats still on top. Roles aren't shown anywhere a team is.
- A meeting logged on a firm takes attendees as free text and never reaches the people: the August roadshow doesn't show on Priya, David or Tom. Correct "LCM" later and anything logged under it is stranded.
- Assigning someone to a firm means opening the person and typing, which is how the duplicates got there. The clean-up is left to Josh, one person at a time.

Against the pitch's "done looks like", none of the three steps works yet. Kept from week 1: the audit line when a person's firm changes, and the import mapping the company column.

## The bet, and what's most likely wrong

If a firm is a record, and the clean-up suggests merges for a person to confirm, Josh will trust the CRM over his sheet. The likeliest thing to be wrong: in this prototype, "log it once, show it on three people" is a few lines; in the real product a meeting is stored against one contact (Exhibit L), so it may mean changing how meetings are stored. First question for Jimmy; it decides whether day 2–3 is a day or a week.

## The calls I made

1. **Organisation is a record**: an id, a name, and the spellings it absorbed. Everything follows from this.
2. **The migration suggests, a person confirms.** Every company string becomes a firm; likely duplicates are flagged (same name once filler words are ignored, or initials); Josh or CS merges each with one click. Nothing auto-merges.
3. **Merged spellings become aliases**, so a later import with "LCM" lands on Larkspur, not a fourth copy.
4. **A meeting is logged once on the firm with attendees ticked**, and shows on the firm and each person.
5. **Organisation on a contact is picked, not typed**: a searchable picker from the contact's page or the list; "create new" is an explicit step.
6. **Role reuses the occupation field**, relabelled.
7. **Creating a firm runs straight into adding its people**, and warns if the name exists or looks like one that does.

## The five days, in order

1. Organisation as a record; contacts point at it. Day 1; everything depends on it.
2. Migration with the review screen, so the data is right before CS or Josh see it. Day 1–2.
3. The organisation page: people with roles, log a meeting with attendees, timeline. Day 2–3. The "done looks like" test.
4. Organisations list in the nav, with merge. Day 3.
5. Contact page: picker, role label, list links. Day 4.
6. Walk CS through it Thursday; fix what they find. Day 5.

## How we'd know it worked

Josh logs the February roadshow on firms, not in the sheet; the Funds tab stops being updated; CS stop hearing "can't group by firm". Countable later: meetings logged on firms per client. Rollout: Corella first, CS running the review; wrong merges stop it before the next client.

## What I left out, and why

- Josh's spreadsheet, the second problem. The failing import is left visible on purpose. A per-firm import template waits for it.
- Organisation type, owner per firm, follow-ups, email audiences by firm, permissions, linking firms to the ownership report (the next bet).
- A written summary per firm: a canned one in a prototype would be a fake.
- General CRM UX: filters, tags, sorting, pagination. Real, not this cycle.

## Questions for Jimmy

- Organisation was built as a text field on each person rather than its own record. Was that a week-one time call, or a reason not to? If we make it a record, how much of the back end changes?
- A meeting is stored against one person today. To show one meeting on a firm and three people, does how meetings are stored have to change, or can it be handled on screen for now?
- In other clients' CRMs, how messy is the company field: dozens of duplicate groups to review, or hundreds?

## What I'd want to learn from Josh

- Does he have an email address for everyone in the Funds tab? The import matches people by email and drops rows without one; his sheet lists names.
- What he does with the Funds tab week to week: roadshows, % held, follow-ups. It decides what the firm page shows first.
- How often one meeting involves more than one firm (the Hartley lunch, the conference). I built one firm per meeting.

## Assumptions

- The pack asked for a one-page plan, no build; the email for a prototype and a note. I followed the email and folded the plan in.
- CS will run the clean-up for clients who won't.
- A firm is the right unit this cycle; funds within a firm are the next bet, as the pitch says.
