from ... import baseAPIurl, BotClient
from ....schema.Channel.ChannelUser import *
from typing import Optional

class channelUser:
    """
    频道消息相关接口列表
    """

    @staticmethod
    async def get_joined_channel(
        guild_id: str,
        user_id: str,
        page: Optional[int] = None,
        page_size: Optional[int] = None
    ) -> channelUserGetJoinedChannelHandler:
        """
        根据用户 id 和服务器 id 获取用户所在语音频道

        :param guild_id: 服务器ID
        :param user_id: 用户ID
        :param page: 目标页数
        :param page_size: 每页数据数量
        """
        data = {
            "page": page,
            "page_size": page_size,
            "guild_id": guild_id,
            "user_id": user_id
        }
        result = await BotClient.get(baseAPIurl + '/channel-user/get-joined-channel', params=data)
        return channelUserGetJoinedChannelHandler(**result.json())