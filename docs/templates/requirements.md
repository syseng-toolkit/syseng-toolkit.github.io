# Requirements

What the system must do, how each requirement flows down from the one above it, and how it will be verified.

**Version 1.0.0**

Released 2026-11-25 · [all releases](https://github.com/syseng-toolkit/syseng-toolkit.github.io/releases)

[Make a copy (Google Sheets)](https://docs.google.com/spreadsheets/d/1z4E65QFozaYRceZlbSY0BEcJGd0UgpfJk-wZZ2N0sGo/copy){ .md-button .md-button--primary } [Download .xlsx](https://github.com/syseng-toolkit/syseng-toolkit.github.io/releases/download/requirements-v1.0.0/syseng-toolkit-requirements-1.0.0.xlsx){ .md-button }

## Tabs

| Tab | What it's for |
|---|---|
| Dashboard (READ ONLY) | Status counts, % verified, by subsystem, verification method and priority, recent changes, and what needs attention. |
| Requirements | The master list. One row per requirement, kept forever. |
| Lists | Dropdown values (subsystems, owners). Change names here once. |
| By Subsystem (READ ONLY) | Pick a subsystem in the yellow cell to see only its requirements. |
| Trace Tree (READ ONLY) | Indented outline of the flow-down, parent → children. |
| Change Log | One line per change to a requirement: date, ID, what changed, was, now, reason, by. History is never overwritten. |
| Document Release | Official released versions of your requirements (v1.0, v1.1…), for example at a design review. |
| Template History | Release notes for this template. The last row is the version your copy is on. |

## Writing good requirements

- **One "shall" per row.** If a sentence asks for two things, split it into two requirements. The Check column flags rows with no "shall".
- **Verifiable.** Someone must be able to check it pass/fail with the chosen Verification method. If it's about a quantity, give the number, units and a tolerance where it applies (0.75 kg, 600 mm, ±0.5°). Requirements that aren't about a quantity ("shall use a USB-C connector") don't need one.
- **No solutions.** Say what is needed, not how to build it.

## Flow-down and links

- **Parent** is the one requirement this one flows down from. Leave it blank for top-level (system) requirements. The parent's **Children** column fills in by itself, and the Trace Tree shows the whole hierarchy.
- **Related** is for loose links to requirements that interact but aren't in the flow-down: a shared constraint, an interface, a derived value. List them comma-separated (`REQ-003, REQ-005`). The other side shows them under **Linked From**.

## Status

| Status | Meaning |
|---|---|
| Draft | Proposed, still being worded. Never agreed. |
| Needs Review | Was agreed, but something it depends on changed, so re-check it before trusting it again. Set by hand. |
| Accepted | The team agrees this is the right requirement. |
| Verified | The Verification method (Test / Design / Analysis / Inspection) was carried out and passed. |
| Obsolete | Retired, kept for history. Never delete a requirement. |

## Logging a change

Add a line at the bottom of the Change Log, newest last (Ctrl+; types today's date). The requirement's Last Changed and # Changes update by themselves. For a change to the content of a requirement that has children, the **Children to check** column lists them, so you can decide whether any need updating. It's a heads-up only; nothing changes automatically.

## Columns

### Requirements tab

| Column | Typed or auto | What goes in it |
|---|---|---|
| ID | Typed | `REQ-###` (the next free ID is on the README). Never reused or renumbered; red if two rows share it. |
| Title | Typed | A short name (2–5 words) used in lists, the Trace Tree and the Dashboard. |
| Requirement (one "shall" statement) | Typed | One "shall" statement that can be checked pass/fail. Number, units and tolerance when it's about a quantity. |
| Subsystem | Typed (dropdown) | Which subsystem owns it. Drives By Subsystem and the Dashboard. |
| Parent | Typed | The one `REQ-###` this flows down from; blank for top level. Drives Children and the Trace Tree. |
| Related | Typed, optional | Comma-separated `REQ-###` that interact with this one but aren't in its flow-down. |
| Priority | Typed (dropdown) | Must / Should / Could. |
| Status | Typed (dropdown) | Draft / Needs Review / Accepted / Verified / Obsolete. |
| Verification | Typed (dropdown) | How it will be proven: Test / Design / Analysis / Inspection. |
| Rationale | Typed | Why this requirement exists and where its number comes from. |
| Owner | Typed (dropdown) | The one person responsible for it. |
| Notes | Typed | Anything else. |
| Children (auto) | Auto | Requirements whose Parent is this one (up to 5, then +N more). |
| Linked From (auto) | Auto | Requirements that list this one under Related. |
| Check (auto) | Auto | Writing and link problems: no text, no "shall", no verification method, a bad Parent or Related ID. Blank means fine. |
| Last Changed (auto) | Auto | Date of this requirement's latest Change Log line. |
| # Changes (auto) | Auto | How many Change Log lines it has. |

### Change Log tab

| Column | Typed or auto | What goes in it |
|---|---|---|
| Date | Typed | Date of the change. Add new lines at the bottom. |
| REQ ID | Typed | The `REQ-###` that changed. |
| What Changed | Typed (dropdown) | Added / Wording / Value / number / Status / Verification / Parent / links / Obsoleted / Other. |
| Was | Typed | The old value or wording. |
| Now | Typed | The new value or wording. |
| Reason | Typed | Why it changed. |
| By | Typed | Who made the change. |
| Title (auto) | Auto | The requirement's title ("ID not found" if there's no such requirement). |
| Children to check (auto) | Auto | That requirement's children, which may need updating after a content change. |

## Google Sheets and Excel

Everything calculates in both. Two extras are Google Sheets only: warning-only protection on the README and READ ONLY tabs, and the bright pink warning when a formula is typed over.

## Release notes

### 1.0.0

First release. Requirements list (REQ-###) with Parent and Related trace links, and automatic Children, Linked From and Check columns. Change Log with Children to check. By Subsystem, Trace Tree and Dashboard views (READ ONLY). Document Release tab for the project's own releases.
