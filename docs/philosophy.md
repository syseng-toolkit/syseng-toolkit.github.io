# Design philosophy

These templates come from building robots with small teams. Each rule below is there because skipping it cost us time.

## Based on ISO/IEC/IEEE 15288, arranged as a V

The templates follow the system life cycle processes of **[ISO/IEC/IEEE 15288:2023](https://sebokwiki.org/wiki/ISO/IEC/IEEE_15288)** (*Systems and software engineering — System life cycle processes*), arranged as a **V-model**. The left side of the V defines the system (stakeholder needs, system requirements, architecture, design), the bottom builds it, and the right side checks each level against what was defined across from it (verification, integration, validation). Templates such as the Task Tracker, the Risk Register and the Document List support the standard's technical management processes, which run through the whole project. [Templates](templates/index.md) shows where each one fits.

The toolkit is *aligned with* the standard, not a way to claim compliance with it. Compliance is a statement about how an organization runs its processes, and no set of templates can make it for you. The toolkit covers the development part of the life cycle for a small team; the standard's agreement and organizational processes, and its later stages (transition, operation, maintenance and disposal), are out of scope for now.

## Spreadsheets, on purpose

Every engineer can open a spreadsheet. There's no tool to install, no license to buy and no data trapped in a format that outlives the vendor. A spreadsheet also shows its work: click any number and you see the formula behind it.

## Works in Excel, not just Google Sheets

Every formula uses functions that both apps support, and each release is checked by downloading it as `.xlsx`. That rules out a lot of convenient Google-only functions, and we think that's the right trade: a team that doesn't use Google, or a company that can't, gets the same templates. Where a Google Sheets extra doesn't carry over (warning-only protection, the pink overwrite warning), the README says so.

## Only as much process as prevents real mistakes

Each template adds the discipline that stops a specific, expensive mistake, and nothing more:

- a requirement that can't be tested → one "shall", a verification method, and a Check column;
- a requirement nobody owns → exactly one owner per requirement;
- a change nobody remembers → a Change Log line for every change, with the reason.

No multi-level requirement databases, no earned-value tracking, no status that changes by itself.

## IDs are forever

IDs like `REQ-###` are never reused or renumbered. Retired items are marked Obsolete, not deleted. A reference written in a meeting note, a commit message or a test report means the same thing a year later.

## One home per document

Each document lives in one place: code in the repository, CAD in the CAD tool, spreadsheets in the project folder. The Document List holds the link to each one, and other documents refer to it by its D-number instead of keeping their own copy of a link.

## You type in white cells

Calculated columns are gray and filled in ahead of time, so there's nothing to drag down and nothing to break by sorting. Every column header has a note saying what goes in it. Every table has alternating row colors, so long rows stay readable.

## Releases you can trust

Each template has its own semantic version, and every copy carries its release notes in the `Template History` tab. You can always tell which version a project is on and what changed since. See [Versions and releases](versions.md).
