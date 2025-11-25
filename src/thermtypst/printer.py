from collections.abc import Callable
from io import BytesIO
import json
from pathlib import Path
from escpos.config import Config
from escpos.capabilities import Profile, get_profile
import typst

from thermtypst.note import Note


def itpp047_profile_override() -> Profile:
    prof: Profile = get_profile("ITPP047")
    prof.profile_data["media"] = {"dpi": 203, "width": {"mm": 80, "pixels": 640}}
    prof_new = Profile(None, prof.features)
    prof_new.profile_data = prof.profile_data
    return prof_new


class PrinterManager:
    def __init__(
        self,
        config_path: Path | None = None,
        profile_override: Profile | None = None,
    ) -> None:
        config = Config()
        config.load(config_path=config_path)
        if profile_override:
            config._printer_config["profile"] = profile_override

        self.printer = config.printer()

    def print_typst_note(self, note: Note, template: Path):
        self._print_image(self._render_note(note, template))

    def _print_image(self, image_data: bytes):
        self.printer.image(BytesIO(image_data))
        self.printer.cut()

    def _render_note(self, note: Note, template: Path) -> bytes:
        note_data = json.dumps(note.typst_data())
        inputs = {"note_data": note_data}
        image = typst.compile(
            template,
            format="png",
            ppi=self.printer.profile.profile_data["media"]["dpi"],
            sys_inputs=inputs,
        )
        return image
