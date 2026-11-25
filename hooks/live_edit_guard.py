"""Local preview only (mkdocs-local.yml): makes mkdocs-live-edit-plugin safe to run.

The plugin's file server takes requests from any web page and any path. This hook:
- accepts only the preview's own pages (http://<dev_addr> and its localhost twin), so another
  site open in the browser can't read, write or delete files;
- refuses any path outside docs/ (e.g. "../mkdocs.yml").
"""

from pathlib import Path

from live import plugin as live
from websockets import serve

Plugin = live.LiveEditPlugin


def _inside_docs(self, path):
    docs = self._get_docs_dir().resolve()
    target = (docs / path).resolve()
    if not target.is_relative_to(docs):
        raise OSError(f"live-edit: {path} is outside docs/")
    return path


def _guard(name, nargs=1):
    original = getattr(Plugin, name)

    def wrapped(self, *args):
        for arg in args[:nargs]:
            _inside_docs(self, arg)
        return original(self, *args)

    setattr(Plugin, name, wrapped)


_guard("read_file_contents")
_guard("write_file_contents")
_guard("delete_file")
_guard("create_new_file")
_guard("rename_file", 2)


def _new_name_in_same_folder(original):
    def wrapped(self, old_filepath, new_filename):
        if Path(new_filename).name != new_filename:
            raise OSError(f"live-edit: {new_filename} must be a plain file name")
        return original(self, old_filepath, new_filename)
    return wrapped


Plugin.rename_file = _new_name_in_same_folder(Plugin.rename_file)


async def _event_loop(self):
    addr = self.mkdocs_config["dev_addr"]
    host = self.config["websockets_host"] or addr.host
    port = addr.port
    origins = [f"http://{addr.host}:{port}", f"http://localhost:{port}", f"http://127.0.0.1:{port}"]
    async with serve(self.websocket_receiver, host, self.config["websockets_port"], origins=origins):
        self.log.info("live-edit (guarded) listening on %s:%d for %s",
                      host, self.config["websockets_port"], ", ".join(sorted(set(origins))))
        await live.asyncio.Future()


Plugin.event_loop = _event_loop
