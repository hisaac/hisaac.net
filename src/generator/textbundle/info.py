from pathlib import Path
import json


class Info:
    def __init__(
        self,
        version: int = 2,
        bundle_type: str = "net.daringfireball.markdown",
        transient: bool = False,
        creator_url: str = None,
        creator_identifier: str = None,
        source_url: str = None,
        application_specific_data: dict = None,
    ):
        self.version = version
        self.bundle_type = bundle_type
        self.transient = transient
        self.creator_url = creator_url
        self.creator_identifier = creator_identifier
        self.source_url = source_url
        self.application_specific_data = application_specific_data

    @classmethod
    def from_path(cls, path: Path):
        contents = path.read_text()
        json_contents = json.loads(contents)
        return cls(
            version=json_contents.get("version"),
            bundle_type=json_contents.get("type"),
            transient=json_contents.get("transient"),
            creator_url=json_contents.get("creatorURL"),
            creator_identifier=json_contents.get("creatorIdentifier"),
            source_url=json_contents.get("sourceURL"),
            application_specific_data=json_contents.get("applicationSpecificData"),
        )
