from .. import Base, statusBase, meta
from ..User import userBase
from typing import Optional, Union, Dict, List

class permissionUsers(Base):
    user: userBase
    allow: int
    deny: int

class permissionOverwrites(Base):
    role_id: int
    allow: int
    deny: int

class permissionUser(Base):
    user_id: str
    allow: int
    deny: int

class channelBase(Base):
    id: str
    guild_id: str
    user_id: str
    parent_id: str
    name: str
    topic: str
    type: int
    level: int
    slow_mode: int
    has_password: bool
    is_category: bool
    permission_sync: int
    permission_overwrites: List[Union[permissionOverwrites, None]]
    permission_users: List[Union[permissionUsers, None]]

class list(statusBase):
    class Data(Base):
        class Items(Base):
            id: str
            user_id: str
            parent_id: str
            name: str
            type: int
            level: int
            limit_amount: int
            is_category: bool
        items: List[Items]
        meta: meta
    data: Data
    
class view(statusBase):
    class Data(channelBase):
        limit_amount: int
        voice_quality: str
        server_url: str
        children: Optional[List[str]]
    data: Data

class create(statusBase):
    data: view.Data

class update(statusBase):
    data: channelBase

class delete(statusBase):
    data: Dict

class userList(statusBase):
    data: List[userBase]

class moveUser(statusBase):
    data: List

class channel_role:
    class index(statusBase):
        permission_sync: int
        permission_overwrites: List[Union[permissionOverwrites, None]]
        permission_users: List[Union[permissionUsers, None]]
    
    class create(statusBase):
        data: Union[permissionOverwrites, permissionUser]

    class update(statusBase):
        data: Union[permissionOverwrites, permissionUser]

    class sync(statusBase):
        class Data:
            permission_overwrites: List[Union[permissionOverwrites, None]]
            permission_users: List[Union[permissionUsers, None]]
        data: Data
    
    class delete(statusBase):
        data: Dict