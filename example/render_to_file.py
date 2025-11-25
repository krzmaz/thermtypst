from datetime import date, time
from escpos.capabilities import Profile
from pathlib import Path
from thermtypst.printer import PrinterManager
from thermtypst.note import BasicNote


TYPST_TEMPLATE = Path(__file__).parent / "typst/main.typ"


def main():
    profile_with_dpi = Profile()
    profile_with_dpi.profile_data["media"]["dpi"] = 203

    p = PrinterManager(
        Path(__file__).parent / "escpos-config.yaml", profile_override=profile_with_dpi
    )
    note = BasicNote(text="Test to-do note", date=date(2025, 1, 1), time=time(9, 00))
    image = p._render_note(note, TYPST_TEMPLATE)
    with open("example.png", "wb") as f:
        f.write(image)


if __name__ == "__main__":
    main()
