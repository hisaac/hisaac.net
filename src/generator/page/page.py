import datetime


class Page:
    title: str
    content: str
    slug: str
    date: datetime
    tags: list[str]
    attributes: dict[str, str]
