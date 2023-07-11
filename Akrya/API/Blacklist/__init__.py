from .. import baseAPIurl, BotClient
from ...schema.Blacklist import *
from typing import Optional

class blacklist():
    """
    黑名单相关接口
    """
    @staticmethod
    async def list(
        guild_id: str
        ) -> blacklistListHandler:
        """
        获取黑名单列表

        :param guild_id: 服务器ID
        :return: blacklistListHandler
        """
        data = {
            "guild_id": guild_id
        }
        result = await BotClient.get(baseAPIurl + '/blacklist/list', params=data)
        return blacklistListHandler(**result.json())

    @staticmethod
    async def create(
        guild_id: str, 
        target_id:str, 
        remark: Optional[str] = None, 
        del_msg_days: Optional[int] = None
    ) -> blacklistCreateHandler:
        """
        加入黑名单
        
        :param guild_id: 服务器ID
        :param target_id: 目标用户ID
        :param remark: 加入黑名单的原因
        :param del_msg_days: 删除最近几天的消息，最大 7 天, 默认 0

        :return: blacklistCreateHandler
        """
        body = {
            "guild_id": guild_id,
            "target_id": target_id
        }
        if remark: body["remark"] = remark
        if del_msg_days: body['del_msg_days'] = del_msg_days
        result = await BotClient.post(baseAPIurl + '/blacklist/create', data=body)
        return blacklistCreateHandler(result)

    @staticmethod
    async def delete(
        guild_id: str, 
        target_id:str
    ) -> blacklistDeleteHandler:
        """
        删除黑名单
        
        :param guild_id: 服务器ID
        :param target_id: 目标用户ID

        :return: blacklistDeleteHandler
        """
        body = {
            "guild_id": guild_id,
            "target_id": target_id
        }
        result = await BotClient.post(baseAPIurl + '/blacklist/delete', data=body)
        return blacklistDeleteHandler(result)
