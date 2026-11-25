# syseng-toolkit

Free systems engineering templates for small hardware teams, starting with a Document List and Requirements. They work in Google Sheets and in Excel.

**User guide and downloads: https://syseng-toolkit.github.io/**

Each template is released on its own, with a semantic version (`requirements-v1.0.0`). Every release is on the [Releases](https://github.com/syseng-toolkit/syseng-toolkit.github.io/releases) page with its `.xlsx` file and release notes.

## Working on the site

```
pip install -r requirements.txt
mkdocs serve
```

To edit pages in the browser while you preview, run the local config instead:

```
pip install -r requirements-local.txt
mkdocs serve -f mkdocs-local.yml
```

Each page then has an edit button (from [mkdocs-live-edit-plugin](https://github.com/eddyluten/mkdocs-live-edit-plugin)) that saves straight to its file in `docs/`. It exists only in this local preview; the public site never has it. `hooks/live_edit_guard.py` lets only the preview's own pages use it, and only on files inside `docs/`. Review your changes with `git diff` before committing, as usual.

Pages are in `docs/`. Pushing to `main` publishes the site (`.github/workflows/pages.yml`).

Template pages that aren't public yet are listed under `exclude_docs` in `mkdocs.yml`: the site skips them. To publish one, delete its line there and add it to `nav`.

**The template list lives in one place: `data/templates.yml`.** The V-model diagram and the template tables on the Home and Templates pages are built from it at build time by `hooks/vmodel.py` (placeholders like `<!-- vmodel -->` in the pages). To add a planned template, release one, or move one to another stage on the V, edit its entry there; the comments at the top of the file explain each field. A typo in a stage name fails the build with a message naming the template.

## License

© 2026 Stephen Mock and Seena Vafaee. The templates and the site are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (full text in [LICENSE](LICENSE)): use them for anything, including commercial work, as long as you credit us. How to credit, and how to ask about other uses: [License page](https://syseng-toolkit.github.io/license/).
