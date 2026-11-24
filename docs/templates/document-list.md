# Document List

The register of every document in a project: one row per document, with its ID, where it lives and a link. If it isn't in the Document List, it doesn't officially exist.

**Version 1.0.0**

<!-- The release step fills in these two links. -->
[Make a copy (Google Sheets)](https://docs.google.com/spreadsheets/d/RELEASE_SHEET_ID/copy){ .md-button .md-button--primary } [Download .xlsx](https://github.com/syseng-toolkit/syseng-toolkit/releases/tag/document-list-v1.0.0){ .md-button }

## Tabs

| Tab | What it's for |
|---|---|
| Document List | One row per document. Add new documents at the bottom. |
| Document Release | One line each time this list is signed off (for example "Release 1 approved"). |
| Template History | Release notes for this template. The last row is the version your copy is on. |

## How to use it

- **Give every document a D-number** (`D-001`, `D-002`…) and a row, including links to things that don't live in the same place: the code repository, the CAD, a folder of drawings.
- **Make this the one place links live.** Other documents refer to each other by D-number, and the Document List holds the link. When a file moves, you update one cell.
- **Never reuse or renumber an ID.** A retired document stays in the list with Status = Obsolete.
- **Release** is the document's own release or version (for example 1.0, 2.1 or Rev A), not the template's.

## Columns

| Column | Typed or auto | What goes in it |
|---|---|---|
| ID | Typed | `D-###`. Never reused or renumbered; turns red if two rows share it. |
| Title | Typed | The document's name, as people call it. |
| Type | Typed | What kind of document it is: Google Sheet, Google Doc, draw.io diagram, repo, CAD, link page… |
| Release | Typed | The document's own release or version (for example 1.0, 2.1 or Rev A). |
| Status | Typed (dropdown) | WIP = being built · Proposed = ready for review · Active = in use · Obsolete = retired (keep the row). |
| Location | Typed | Where it lives: a folder (e.g. `01-Systems`), the project repo, or the CAD tool. |
| Link | Typed | A link to open it. `=HYPERLINK("url","Open")` keeps the cell short. |
| Created By | Typed | Who made it. |
| Date Added | Typed | Date it was added to this list. |
| Notes | Typed | Anything else, for example what it replaces. |

## Google Sheets and Excel

Everything works in both. In Google Sheets the README tab warns before you edit it; Excel has no warning-only protection.

## Release notes

### 1.0.0

First release. One row per project document (D-###): title, type, release, status, location, link, created by, date added, notes. Document Release tab for the project's own releases.
