from .. import BotClient, baseAPIurl
from ...schema.User import *
from typing import Optional

class user:
    """
    用户相关接口
    """
    @staticmethod
    async def me() -> userMeHandler:
        '''
        获取当前用户信息

        :return: userMeHandler
        '''
        result = await BotClient.get(url=baseAPIurl + "/user/me")
        return userMeHandler(**result.json())

    @staticmethod
    async def view(
        user_id: str, 
        guild_id: Optional[str] = None
    ) -> userViewHandler:
        '''
        获取目标用户信息

        :param user_id: 用户id
        :param guild_id: (可选)服务器id

        :return: userViewHandler
        '''
        data = {
            "user_id": user_id
        }
        if guild_id:
            data["guild_id"] = guild_id
        result = await BotClient.get(url=baseAPIurl + "/user/view", params=data)
        return userViewHandler(**result.json())

    @staticmethod
    async def offline() -> userOfflineHandler:
        '''
        下线机器人

        :return: userOfflineHandler
        '''
        result = await BotClient.post(url=baseAPIurl + "/user/offline")
        return userOfflineHandler(**result.json())

