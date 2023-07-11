from ...schema import Base, statusBase
from ...schema.objects import userBase
from typing import List

class Data(Base):
    class Item(Base):
        channel_id: str
        guild_id: str
        url_code: str
        url: str
        user: userBase

    items: List[Item]

    class Meta(Base):
        page: int
        page_total: int
        page_size: int
        total: int

    meta: Meta


class inviteListHandler(statusBase):
    data: Data


class inviteCreateHandler(statusBase):
    class Data(Base):
        url: str

    data: Data


class inviteDeleteHandler(statusBase):
    data: dict
