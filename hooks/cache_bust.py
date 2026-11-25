"""Version-stamp the site's own CSS and JS links (extra.css?v=3f9a1c2b), so a browser fetches the
new file as soon as it changes instead of using a cached copy for up to 10 minutes (GitHub Pages).

The stamp is a short hash of the file's contents: it only changes when the file does.
Covers every entry in extra_css and extra_javascript in mkdocs.yml.
"""

import hashlib
import os
import re

_stamps = {}


def on_config(config):
    _stamps.clear()
    for entry in list(config["extra_css"]) + [getattr(e, "path", e) for e in config["extra_javascript"]]:
        path = str(entry)
        src = os.path.join(config["docs_dir"], path)
        if os.path.isfile(src):
            with open(src, "rb") as f:
                _stamps[path] = hashlib.sha256(f.read()).hexdigest()[:8]
    return config


def on_post_page(output, page, config):
    for path, stamp in _stamps.items():
        # href="../stylesheets/extra.css" or src="javascripts/sheet-preview.js": add ?v= once
        output = re.sub(rf'((?:href|src)="[^"?]*{re.escape(path)})"', rf'\1?v={stamp}"', output)
    return output
