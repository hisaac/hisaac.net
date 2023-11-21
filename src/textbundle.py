import json
import pathlib


class Info:
	def __init__(
			self,
			version: int = 2,
			bundle_type: str = "net.daringfireball.markdown",
			transient: bool = False,
			creator_url: str = None,
			creator_identifier: str = None,
			source_url: str = None,
			application_specific_data: dict = None
	):
		self.version = version
		self.bundle_type = bundle_type
		self.transient = transient
		self.creator_url = creator_url
		self.creator_identifier = creator_identifier
		self.source_url = source_url
		self.application_specific_data = application_specific_data

	@classmethod
	def from_path(cls, path: pathlib.Path):
		contents = path.read_text()
		json_contents = json.loads(contents)
		return cls(
			version=json_contents.get("version"),
			bundle_type=json_contents.get("type"),
			transient=json_contents.get("transient"),
			creator_url=json_contents.get("creatorURL"),
			creator_identifier=json_contents.get("creatorIdentifier"),
			source_url=json_contents.get("sourceURL"),
			application_specific_data=json_contents.get("applicationSpecificData")
		)


class Text:
	def __init__(self, text: str):
		self.text = text

	@classmethod
	def from_path(cls, path: pathlib.Path):
		return cls(text=path.read_text())


class Assets:
	def __init__(self, files: list[pathlib.Path] = None):
		self.files = files

	@classmethod
	def from_path(cls, path: pathlib.Path):
		files = path.glob('**/*')
		return cls(files=list(files))


class TextBundle:
	def __init__(
			self,
			path: pathlib.Path,
			info: Info,
			text: Text,
			assets: Assets = None
	):
		self.path = path
		self.info = info
		self.text = text
		self.assets = assets

	@classmethod
	def from_path(cls, path: pathlib.Path):
		info_path = path.joinpath('info.json')
		text_path = path.joinpath('text.md')
		assets_path = path.joinpath('assets')
		return cls(
			path=path,
			info=Info.from_path(path=info_path),
			text=Text.from_path(path=text_path),
			assets=Assets.from_path(path=assets_path)
		)
