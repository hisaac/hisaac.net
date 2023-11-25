from pathlib import Path

from .textbundle import Info, Text, Assets


class TextBundle:
    def __init__(
        self,
        path: Path,
        info: Info,
        text: Text,
        assets: Assets = None,
    ):
        self.path = path
        self.info = info
        self.text = text
        self.assets = assets

    @classmethod
    def from_path(cls, path: Path):
        info_path = path.joinpath("info.json")
        text_path = path.joinpath("text.md")
        assets_path = path.joinpath("assets")
        return cls(
            path=path,
            info=Info.from_path(path=info_path),
            text=Text.from_path(path=text_path),
            assets=Assets.from_path(path=assets_path),
        )
