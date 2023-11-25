from pathlib import Path


class Assets:
    def __init__(self, files: list[Path] = None):
        self.files = files

    @classmethod
    def from_path(cls, path: Path):
        files = path.glob("**/*")
        return cls(files=list(files))
