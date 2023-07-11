from ...schema import Base,statusBase
from typing import List

class User(Base):
    id:str
    username:str
    identify_num:str
    online:bool
    status:int
    bot:bool
    avatar:str
    vip_avatar:str

class Data(Base):
    class Item(Base):
        channel_id:str
        guild_id:str
        url_code:str
        url:str
        user:User
    items:List[Item]
    class Meta(Base):
        page:int
        page_total:int
        page_size:int
        total:int
    meta:Meta
    
class getInvitelist(statusBase):
    data:Data
    
class createInvite(statusBase):
    class data(Base):
        url:str
    data:data

class  deleteInvite(statusBase):
    data:dict