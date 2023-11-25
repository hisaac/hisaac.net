from pathlib import Path


class text:
    def __init__(self, text: str):
        self.text = text

    @classmethod
    def from_path(cls, path: Path):
        return cls(text=path.read_text())
