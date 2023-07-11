from .. import baseAPIurl, BotClient
from ...schema.Channel import *
from typing import Optional

class channel:
    """
    频道相关接口列表
    """

    @staticmethod
    async def list(page: Optional[int] = None, page_size: Optional[int] = None, guild_id: Optional[str] = None, type: Optional[int] = None):
        """
        获取频道列表
        """