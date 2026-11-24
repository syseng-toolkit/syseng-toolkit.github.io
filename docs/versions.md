# Versions and releases

Each template has its own version number, so a fix to one template doesn't change the others.

## Version numbers

Versions follow [semantic versioning](https://semver.org): `MAJOR.MINOR.PATCH`.

| Change | Example | What it means for your copy |
|---|---|---|
| **MAJOR** | 1.4.2 → 2.0.0 | Something was renamed, moved or removed (a column or a tab). Read the release notes before updating a project that already has data. |
| **MINOR** | 1.4.2 → 1.5.0 | A new feature, such as a new calculated column or view. Your data still reads the same. |
| **PATCH** | 1.4.2 → 1.4.3 | A fix, a clearer README or better examples. |

## Which version do I have?

Open the `Template History` tab in your copy. Each row is one release, and the last row is your version. Each row lists new features, bug fixes, breaking changes and anything else worth knowing.

## Where releases live

Every release is on the GitHub [Releases page](https://github.com/syseng-toolkit/syseng-toolkit.github.io/releases), tagged by template and version (for example `requirements-v1.0.0`), with its `.xlsx` file and release notes. Older versions stay there, so you can always get the exact file a project started from.

The **Make a copy** button on each template page always points to the latest release.

## Updating a project to a new version

Templates are copied, not linked, so a project's copy doesn't change when a new version comes out. To update one:

1. Read the release notes for every version since yours (your version is the last row of `Template History`).
2. Make the same changes in your copy: new columns, formulas or rules. Don't copy a whole tab over your project's tab, because that replaces your data.
3. Add the release's row to your `Template History`.

You don't have to update. A project can stay on the version it started with.
