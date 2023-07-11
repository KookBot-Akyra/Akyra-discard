from ... import statusBase, Base, meta
from ...objects import channelBase
from typing import List

class get_joined_channel(statusBase):
    class Data(Base):
        items: List[channelBase]
        meta: meta
    data: Data