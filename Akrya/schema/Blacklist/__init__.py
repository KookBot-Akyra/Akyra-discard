from .. import statusBase, Base, meta
from ..objects import userBase
from typing import List, Dict

class getList(statusBase):
    class Data(Base):
        class Items(Base):
            user_id: str
            created_time: int
            remark: str
            user: userBase
        items: List(Items)
        meta: meta

    data: Data

class create(statusBase):
    data: Dict

class delete (statusBase):
    data: Dict
