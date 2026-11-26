"""Builds the V-model diagram and the template tables from data/templates.yml.

Placeholders a page can use (each on its own line):
  <!-- vmodel -->                  the V-model diagram
  <!-- templates-table:home -->    released and coming-soon templates: name, what it's for, release
  <!-- templates-table:stage -->   templates placed along the V: name, stage, release
  <!-- templates-table:project --> templates for the whole project: name, what it does, release
"""
import html
import os
import re
import posixpath

import yaml

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "templates.yml")
LABEL = {"released": None, "soon": "Coming&nbsp;soon", "planned": "Planned"}
SUFFIX = {"released": "", "soon": " · soon", "planned": " · planned"}


def load():
    with open(DATA, encoding="utf-8") as f:
        return yaml.safe_load(f)


def places(t):
    w = t.get("where", [])
    return w if isinstance(w, list) else [w]


def href(page_url, key):
    """URL of a template page, relative to the page being built (raw HTML isn't rewritten by MkDocs)."""
    here = "/" + (page_url or "")
    if not here.endswith("/"):
        here = posixpath.dirname(here) + "/"
    return posixpath.relpath(f"/templates/{key}/", here) + "/"


def label(t, x, y, anchor, page_url, size=14, bold=True, text=None):
    text = html.escape(text or (t["name"] + SUFFIX[t["status"]]))
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    style = "" if (size == 14 and bold) else f' style="font-size:{size}px;font-weight:{700 if bold else 400}"'
    if t["status"] == "released":
        return f'<a href="{href(page_url, t["key"])}"><text class="tpl" x="{x}" y="{y}"{a}{style}>{text}</text></a>'
    return f'<text class="tpl soon" x="{x}" y="{y}"{a}{style}>{text}</text>'


def vmodel_svg(data, page_url):
    st = data["stages"]
    left, right, n = st["left"], st["right"], len(st["left"])
    top, bottom_y, step_x, step_y = 50, 300, 50, (250 - 50) / max(n - 1, 1)
    lx = lambda i: 165 + i * step_x
    ly = lambda i: top + i * step_y
    rx = lambda i: 595 - (n - 1 - i) * step_x  # right[i] pairs with left[i] counted from the bottom
    ry = lambda i: ly(n - 1 - i)
    bx = 380
    out = ['<svg class="vmodel" viewBox="0 0 800 400" role="img" aria-label="V-model: where each template fits">',
           '<text class="side" x="150" y="22" text-anchor="middle">Define and design ↓</text>',
           '<text class="side" x="610" y="22" text-anchor="middle">↑ Integrate and verify</text>']
    pts = [(lx(i), ly(i)) for i in range(n)] + [(bx, bottom_y)] + [(rx(i), ry(i)) for i in range(n)]
    out.append('<polyline class="arm" points="' + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + '"/>')
    for i in range(1, n):  # dashed links between paired levels (not the top one: needs vs validation)
        out.append(f'<line class="link" x1="{lx(i):.0f}" y1="{ly(i):.0f}" x2="{rx(n - 1 - i):.0f}" y2="{ly(i):.0f}"/>')
    out += [f'<circle class="dot" cx="{x:.0f}" cy="{y:.0f}" r="6"/>' for x, y in pts]
    for i, name in enumerate(left):
        out.append(f'<text class="stage" x="{lx(i) - 12:.0f}" y="{ly(i) + 5:.0f}" text-anchor="end">{html.escape(name)}</text>')
    out.append(f'<text class="stage" x="{bx}" y="{bottom_y + 25}" text-anchor="middle">{html.escape(st["bottom"])}</text>')
    for i, name in enumerate(right):
        out.append(f'<text class="stage" x="{rx(i) + 12:.0f}" y="{ry(i) + 5:.0f}">{html.escape(name)}</text>')
    # templates under their stages
    stacked = {}
    band, tests = [], []
    for t in data["templates"]:
        for p in places(t):
            if p == "project":
                band.append(t)
            elif p == "tests":
                tests.append(t)
            else:
                side, stage = p.split(":", 1)
                stacked.setdefault((side, stage), []).append(t)
    for (side, stage), ts in stacked.items():
        names = left if side == "left" else right
        if stage not in names:
            raise ValueError(f"templates.yml: unknown stage {stage!r} for {ts[0]['name']}")
        i = names.index(stage)
        x, y0 = (lx(i) - 12, ly(i) + 5) if side == "left" else (rx(i) + 12, ry(i) + 5)
        y = y0
        for t in ts:
            y += 19
            out.append(label(t, round(x), round(y), "end" if side == "left" else "start", page_url))
            if side == "right" and t.get("right_note"):
                y += 16
                out.append(f'<text class="soon" x="{round(x)}" y="{round(y)}" style="font-size:12px">{html.escape(t["right_note"])}</text>')
    if tests:  # bracket across every test level
        y1, y2 = ry(n - 2) - 5, ry(0) + 5
        out.append(f'<path class="link" style="stroke-dasharray:none;fill:none" d="M 688 {y1:.0f} h 8 v {y2 - y1:.0f} h -8"/>')
        y = (y1 + y2) / 2 - 20
        for t in tests:
            for part in t["name"].split(" & ", 1) if len(t["name"]) > 12 else [t["name"]]:
                out.append(label(t, 706, round(y), "start", page_url, text=part if part == t["name"].split(" & ")[0] else "& " + part))
                y += 18
            if t["status"] != "released":
                out.append(f'<text class="soon" x="706" y="{round(y)}" style="font-size:12px">{t["status"]},</text>')
                y += 15
            out.append(f'<text class="soon" x="706" y="{round(y)}" style="font-size:12px">all {len(right) - 1} test levels</text>')
            y += 24
    if band:
        out.append('<rect class="band" x="40" y="345" width="680" height="44" rx="8"/>')
        band_label = st.get("band", "Across the whole project") + ":"
        out.append(f'<text class="stage" x="60" y="372">{html.escape(band_label)}</text>')
        x = 60 + int(len(band_label) * 7.2) + 24
        for t in band:
            out.append(label(t, x, 372, "start", page_url))
            x += int(len(t["name"] + SUFFIX[t["status"]]) * 8.2) + 30
    out.append("</svg>")
    return "\n".join(out)


def link(t, page_src):
    if t["status"] != "released":
        return t["name"]
    target = f"templates/{t['key']}.md"
    rel = posixpath.relpath(target, posixpath.dirname(page_src) or ".")
    return f"[{t['name']}]({rel})"


def release(t):
    return t.get("version") if t["status"] == "released" else LABEL[t["status"]]


REPO = "https://github.com/syseng-toolkit/syseng-toolkit.github.io"


def downloads(t):
    """(Google Sheets copy link, .xlsx link) for a released template, from its sheet and version."""
    if not t.get("sheet"):
        raise ValueError(f"templates.yml: released template {t['name']!r} needs a sheet: (the released copy's ID)")
    v, k = t["version"], t["key"]
    return (f"https://docs.google.com/spreadsheets/d/{t['sheet']}/copy",
            f"{REPO}/releases/download/{k}-v{v}/syseng-toolkit-{k}-{v}.xlsx")


def get_it(t):
    if t["status"] != "released":
        return ""
    copy, xlsx = downloads(t)
    k = t["key"]
    return (f"[Sheets]({copy}){{ target=_blank rel=noopener data-goatcounter-click=copy-{k} }} · "
            f"[Excel]({xlsx}){{ data-goatcounter-click=xlsx-{k} }}")


def released(data, key, what):
    t = next((t for t in data["templates"] if t.get("key") == key and t["status"] == "released"), None)
    if t is None:
        raise ValueError(f"{what}: no released template with key {key!r} in templates.yml")
    return t


def view_url(t):
    """The released Sheet's read-only live view, opened on its main tab (tab: gid, default 0)."""
    if not t.get("sheet"):
        raise ValueError(f"templates.yml: released template {t['name']!r} needs a sheet:")
    return f"https://docs.google.com/spreadsheets/d/{t['sheet']}/htmlview?widget=true&headers=false&gid={t.get('tab', 0)}"


def preview(data, key):
    t = released(data, key, "template-preview")
    # Wide screens: the live Sheet inline. Phones: a zoomed-out thumbnail that opens it in the
    # pop-up (sheet-preview.js), since an inline Sheet is too cramped to read or scroll there.
    view, name = view_url(t), t["name"]
    return (f'<iframe class="sheet-preview" src="{view}" loading="lazy" title="{name} template, live view"></iframe>'
            f'<a class="sheet-peek sheet-preview-phone" href="{view}" data-title="{name}">'
            f'<span class="tg-thumb"><iframe src="{view}" loading="lazy" tabindex="-1" title="{name} template, preview"></iframe></span>'
            f'<span class="sheet-preview-tap">Tap to open the live template</span></a>')


def gallery(data, page_url):
    """Home page: a sideways-scrolling strip of live, zoomed-out previews, one card per released
    template. The preview opens the pop-up (docs/javascripts/sheet-preview.js); the name opens
    the template's page."""
    cards = []
    for t in data["templates"]:
        if t["status"] != "released":
            continue
        name, view, page = html.escape(t["name"]), html.escape(view_url(t)), href(page_url, t["key"])
        cards.append(
            '<div class="tg-card">'
            f'<a class="tg-thumb sheet-peek" href="{view}" data-title="{name}" data-page="{page}" '
            f'target="_blank" rel="noopener" aria-label="Preview the {name} template">'
            f'<iframe src="{view}" loading="lazy" tabindex="-1" aria-hidden="true" title="{name}"></iframe></a>'
            f'<a class="tg-cap" href="{page}"><strong>{name}</strong><span class="tg-go">Template page →</span></a>'
            '</div>')
    return ('<div class="tpl-gallery">'
            '<button type="button" class="tg-nav tg-prev" aria-label="Previous templates">&#8249;</button>'
            f'<div class="tg-track">{"".join(cards)}</div>'
            '<button type="button" class="tg-nav tg-next" aria-label="More templates">&#8250;</button>'
            '</div>')


def buttons(data, key):
    copy, xlsx = downloads(released(data, key, "template-buttons"))
    # data-goatcounter-click: counted as an event when analytics is on (overrides/main.html)
    return (f"[Make a copy (Google Sheets)]({copy}){{ .md-button .md-button--primary target=_blank rel=noopener data-goatcounter-click=copy-{key} }} "
            f"[Download .xlsx]({xlsx}){{ .md-button data-goatcounter-click=xlsx-{key} }}")


def table(data, kind, page_src):
    ts = data["templates"]
    if kind == "home":
        rows = [t for t in ts if t["status"] != "planned"]
        head = "| Template | What it's for | Release | Downloads |\n|---|---|---|---|"
        body = [f"| {link(t, page_src)} | {t['about']} | {release(t)} | {get_it(t)} |" for t in rows]
    elif kind == "stage":
        rows = [t for t in ts if places(t) and places(t)[0] != "project"]
        head = "| Template | What it covers | Release | Downloads |\n|---|---|---|---|"
        body = [f"| {link(t, page_src)} | {t.get('stage', t['about'])} | {release(t)} | {get_it(t)} |" for t in rows]
    elif kind == "project":
        rows = [t for t in ts if "project" in places(t)]
        head = "| Template | What it does | Release | Downloads |\n|---|---|---|---|"
        body = [f"| {link(t, page_src)} | {t['about']} | {release(t)} | {get_it(t)} |" for t in rows]
    else:
        raise ValueError(f"unknown table {kind!r}")
    return "\n".join([head] + body)


def on_page_markdown(markdown, page, config, files):
    if not any(m in markdown for m in ("<!-- vmodel -->", "<!-- templates-table:", "<!-- template-buttons:", "<!-- template-preview:", "<!-- templates-gallery -->")):
        return markdown
    data = load()
    src = page.file.src_uri
    markdown = markdown.replace("<!-- vmodel -->", vmodel_svg(data, page.url))
    for kind in ("home", "stage", "project"):
        markdown = markdown.replace(f"<!-- templates-table:{kind} -->", table(data, kind, src))
    markdown = re.sub(r"<!-- template-buttons:([\w-]+) -->", lambda m: buttons(data, m.group(1)), markdown)
    markdown = markdown.replace("<!-- templates-gallery -->", gallery(data, page.url))
    markdown = re.sub(r"<!-- template-preview:([\w-]+) -->", lambda m: preview(data, m.group(1)), markdown)
    return markdown
