from .. import BotClient, baseAPIurl
from ...schema.Invite import *
from typing import Optional


class invite:
    """
    邀请相关接口
    """
    
    @staticmethod
    async def list(
        guild_id: Optional[str] = None, 
        channel_id: Optional[str] = None, 
        page: Optional[int] = None,
        page_size: Optional[int] = None
    ) -> inviteListHandler:
        """
        获取邀请列表
        :Params: guild_id: 服务器ID
        :Params: channel_id 频道ID
        // guild ID && Channel ID 二选一
        :Params: page 页码
        :Params: page_size 每页数据数量
        :return: inviteListHandler
        """
        data = {
            "guild_id": guild_id,
            "channel_id": channel_id,
            "page": page,
            "page_size": page_size
        }
        result = await BotClient.get(url=baseAPIurl + "/invite/list", params=data)
        return inviteListHandler(**result.json())

    @staticmethod
    async def create(
        guild_id: Optional[str] = None, 
        channel_id: Optional[str] = None, 
        duration: Optional[int] = None,          
        setting_times: Optional[int] = None
    ) -> inviteCreateHandler:
        """
        创建邀请列表
        :Params: guild_id: 服务器ID
        :Params: channel_id 频道ID
        // guild ID && Channel ID 二选一
        :Params: duration   邀请链接有效时长（秒)
        :Params: setting_times 设置的次数
        :return: inviteCreateHandler
        """
        data = {
            "guild_id": guild_id,
            "channel_id": channel_id,
            "duration": duration,
            "setting_times": setting_times
        }
        result = await BotClient.post(url=baseAPIurl + "/invite/create", data=data)
        return inviteCreateHandler(**result.json())


    @staticmethod
    async def delete(
        url_code: str, 
        channel_id: Optional[str] = None, 
        guild_id: Optional[str] = None
    ) -> inviteDeleteHandler:
        """
        删除邀请列表

        :Params: url_code 	邀请码
        :Params: channel_id 服务器ID
        :Parmas: guild_id 服务器频道ID
        :return: inviteDeleteHandler
        """
        data = {
            "url_code": url_code,
            "channel_id": channel_id,
            "guild_id": guild_id
        }
        result = await BotClient.post(url=baseAPIurl + "/invite/delete", data=data)
        return inviteDeleteHandler(**result.json())
