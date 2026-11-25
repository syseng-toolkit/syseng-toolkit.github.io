# Design philosophy

## For small teams

The templates are for teams of 3 to 10 people, and for "hobbyists who want to do it a little better". The templates are meant to be easy to port and trace with a small team, but are not meant to scale like enterprise software.

## Learn it in five minutes

Every template has a README tab that explains its tabs and rules but the templates should be relatively easy to follow. Users do not need specific trainings as the tools aim to be simple and straight forward. Each column has a note which contains additional information to guide users. 

## No proprietary software

Every engineer can open a spreadsheet. There's no tool to install, no license to buy and no data trapped in a format that outlives the vendor. 

The templates work the same in Google Sheets and in Excel. Every formula uses functions both apps aim to support.

## Free and open

The templates and this site are free under [CC BY 4.0](license.md): use them for anything, including commercial work, change them to fit your team, and share them, as long as you credit the toolkit. Ideas and fixes are welcome as [issues on GitHub](https://github.com/syseng-toolkit/syseng-toolkit.github.io/issues).

---

## How the templates hold together

### Based on ISO/IEC/IEEE 15288, arranged as a V

The templates follow the system life cycle processes of **[ISO/IEC/IEEE 15288:2023](https://sebokwiki.org/wiki/ISO/IEC/IEEE_15288)** (*Systems and software engineering — System life cycle processes*), arranged as a **V-model**. The left side of the V defines the system (stakeholder needs, system requirements, architecture, design), the bottom builds it, and the right side checks each level against what was defined across from it (verification, integration, validation). Templates such as the Task Tracker, the Risk Register and the Document List support the standard's technical management processes, which run through the whole project. [Templates](templates/index.md) shows where each one fits.

The toolkit is *aligned with* the standard, not a way to claim compliance with it.

### IDs are forever

IDs like `REQ-###` are never reused or renumbered. Retired items are marked Obsolete, not deleted. 

### One home per document

Each document lives in one place: code in the repository, CAD in the CAD tool, spreadsheets in the project folder. The Document List holds the link to each one, and other documents refer to it by its D-number instead of keeping their own copy of a link.

### Release Structure

Each template has its own semantic version, and every copy carries its release notes in the `Template History` tab. You can always tell which version a project is on and what changed since. See [Versions and releases](versions.md).
