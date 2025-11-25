from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import date, time


class Note(ABC):
    @abstractmethod
    def typst_data(self) -> dict: ...


@dataclass
class BasicNote(Note):
    text: str
    date: date | None = None
    time: time | None = None
    flip: bool = False

    def typst_data(self) -> dict:
        data = asdict(self)
        data["date"] = "" if not self.date else self.date.strftime("%d-%m-%Y")
        data["time"] = "" if not self.time else self.time.strftime("%H:%M")
        return data
