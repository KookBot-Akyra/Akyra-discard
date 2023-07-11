from .. import BotClient, baseAPIurl
from ...schema.User import *
from typing import Optional

class user:
    """
    用户相关接口
    """
    @staticmethod
    async def me() -> meHandler:
        '''
        获取当前用户信息

        :return: User.meHandler
        '''
        result = await BotClient.get(url=baseAPIurl + "/user/me")
        return meHandler(**result.json())

    @staticmethod
    async def view(user_id: str, guild_id: Optional[str] = None) -> viewHandler:
        '''
        获取目标用户信息

        :param user_id: 用户id
        :param guild_id: (可选)服务器id

        :return: User.viewHandler
        '''
        data = {
            "user_id": user_id
        }
        if guild_id:
            data["guild_id"] = guild_id
        result = await BotClient.get(url=baseAPIurl + "/user/view", params=data)
        return viewHandler(**result.json())

    @staticmethod
    async def offline() -> offlineHandler:
        '''
        下线机器人

        :return: User.offlineHandler
        '''
        result = await BotClient.post(url=baseAPIurl + "/user/offline")
        return offlineHandler(**result.json())

