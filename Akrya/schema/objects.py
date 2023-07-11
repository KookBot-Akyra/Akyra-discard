from . import Base, statusBase
from typing import Optional, Union, List

class userBase(Base):
    class liveInfo(Base):
        in_live: bool
        audience_count: int
        live_thumb: str
        live_start_time: int

    id: str
    username: str
    nickname: str
    identify_num: str
    online: bool
    bot: bool
    status: int
    avatar: str
    vip_avatar: str
    mobile_verified: Optional[bool]
    roles: List[int]
    joined_at: Optional[int]
    active_time: Optional[int]
    live_info: Optional[liveInfo]

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

class guildBase(Base):
    class Channels(Base):
        id: str
        user_id: str
        parent_id: str
        name: str
        type: int
        level: int
        limit_amount: int
        is_category: bool
    id: str
    name: str
    topic: str
    user_id: str
    icon: str
    notify_type: int
    region: str
    enable_open: bool
    open_id: str
    default_channel_id: str
    welcome_channel_id: str
    roles: str
    channels: List[Channels]

class quoteBase(Base):
    id: str
    type: int
    content: str
    create_at: int
    author: userBase

class attachmentsBase(Base):
    type: str
    url: str
    name: str
    size: int