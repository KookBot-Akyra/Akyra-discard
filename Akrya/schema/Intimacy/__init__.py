from ...schema import Base,statusBase
from typing import List


class imgListStruct(Base):
    id:int
    url:str

class intimacy(Base):
    img_url:str
    social_info:str
    last_read:int
    score:int
    img_list:List[imgListStruct]

class intimacyHandler(statusBase):
    data: intimacy


class updateIntimacyHandler(statusBase):
    data:dict
