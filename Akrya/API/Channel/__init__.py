from .. import baseAPIurl, BotClient
from ...schema.Channel import *
from typing import Optional

class channel:
    """
    频道相关接口
    """

    @staticmethod
    async def list(
        guild_id: str, 
        page: Optional[int] = 1, 
        page_size: Optional[int] = 50, 
        type: Optional[int] = 1
    ) -> channelListHandler:
        """
        获取频道列表

        :param guild_id: 服务器ID
        :param page: (可选)目标页数
        :param page_size: (可选)每页数据数量
        :type: (可选)频道类型. 1为文字, 2为语音, 默认为1

        :return: channelListHandler
        """
        if int(type) not in [1, 2]:
            raise channelVauleError('不支持的类型')
        data = {
            "guild_id": guild_id,
            "page": page,
            "page_size": page_size,
            "type": type
        }
        result = await BotClient.get(baseAPIurl + '/channel/list', params=data)
        return channelListHandler(**result.json())

    @staticmethod
    async def view(
        target_id: str, 
        need_children: Optional[bool]
    ) -> channelViewHandler:
        """
        获取频道详情

        :param traget_id: 频道ID
        :need_children: 是否需要获取子频道

        :return: channelViewHandler
        """
        data = {
            "target_id": target_id,
            "need_children": need_children
        }
        result = await BotClient.get(baseAPIurl + '/channel/view', params=data)
        return channelViewHandler(**result.json())

    @staticmethod
    async def create(
        guild_id: str, 
        name: str, 
        parent_id: Optional[str] = None, 
        type: Optional[int] = 1, 
        limit_amount: Optional[int] = 50, 
        voice_quality: Optional[int] = 2, 
        is_category: Optional[int] = 0
    ) -> channelCreateHandler:
        """
        创建频道

        :param guild_id: 服务器ID
        :param name: 频道名称
        :param parent_id: (可选)父分组ID
        :param type: (可选)频道类型. 1 文字, 2 语音, 默认为 1
        :param limit_amount: (可选)语音频道人数限制. 最大99, 默认50
        :param voice_quality: (可选)语音音质. 1流畅, 2正常, 3高质量. 默认为2
        :param is_category: (可选)是否分组. 1 是, 0 否. 默认为 0

        :return: channelCreateHandler
        """
        if type not in [1, 2]:
            raise channelVauleError('不支持的类型')
        if limit_amount < 0 or limit_amount > 99:
            raise channelVauleError('语音频道人数超出限制')
        if voice_quality not in [1, 2, 3]:
            raise channelVauleError('不支持的语音音质')
        if type == 2:
            data = {
                "guild_id": guild_id,
                "name": name,
                "type": type,
                "limit_amount": limit_amount,
                "voice_quality": str(voice_quality),
                "is_category": is_category
            }
        elif type == 1:
            data = {
                "guild_id": guild_id,
                "name": name,
                "type": type,
                "is_category": is_category
            }
        if parent_id: data["parent_id"] = parent_id
        result = await BotClient.post(baseAPIurl + '/channel/create', data=data)
        return channelCreateHandler(**result.json())

    @staticmethod
    async def update(
        channel_id: str, 
        name: Optional[str] = None, 
        parent_id: Optional[str] = None, 
        limit_amount: Optional[int] = None, 
        voice_quality: Optional[int] = None, 
        level: Optional[int] = None,
        topic: Optional[str] = None,
        slow_mode: Optional[int] = None,
        password: Optional[str] = None,
    ) -> channelUpdateHandler:
        """
        编辑频道

        :param channel_id: 服务器中频道的 ID
        :param name: (可选)频道名
        :param parent_id: (可选)分组频道ID, 设置为0则移除分组
        :param limit_amount: (可选)此频道最大能容纳的用户数量, 最大值 99, 语音频道有效
        :param voice_quality: (可选)语音音质. 1流畅, 2正常, 3高质量. 默认为2, 语音频道有效
        :param level: (可选)频道排序
        :param topic: (可选)频道简介, 文字频道有效
        :param slow_mode: (可选)慢速模式, 单位 ms. 目前只支持这些值：0, 5000, 10000, 15000, 30000, 60000, 120000, 300000, 600000, 900000, 1800000, 3600000, 7200000, 21600000, 文字频道有效
        :param password: (可选)密码, 语音频道有效
        
        :return: channelUpdateHandler
        """
        if limit_amount < 0 or limit_amount > 99:
            raise channelVauleError('语音频道人数超出限制')
        if voice_quality not in [1, 2, 3]:
            raise channelVauleError('不支持的语音音质')
        if slow_mode not in [0, 5000, 10000, 15000, 30000, 60000, 120000, 300000, 600000, 900000, 1800000, 3600000, 7200000, 21600000]:
            raise channelVauleError('不支持的值')
        data = {
            "channel_id": channel_id,
            "name": name,
            "parent_id": parent_id,
            "limit_amount": limit_amount,
            "voice_quality": voice_quality,
            "level": level,
            "topic": topic,
            "slow_mode": slow_mode,
            "password": password
        }
        result = await BotClient.post(baseAPIurl + '/channel/update', data=data)
        return channelUpdateHandler(**result.json())

    @staticmethod
    async def delete(
        channel_id: str
    ) -> channelDeleteHandler:
        """
        删除频道

        :param channel_id: 频道ID

        :return: channelDeleteHandler
        """
        data = {
            "channel_id": channel_id
        }
        result = await BotClient.post(baseAPIurl + '/channel/delete', data=data)
        return channelDeleteHandler(**result.json())

    @staticmethod
    async def userList(
        channel_id: str
    ) -> channelUserListHandler:
        """
        语音频道用户列表

        :param channel_id: 频道ID
        :return: channelUserListHandler
        """
        data = {
            "channel_id": channel_id
        }
        result = await BotClient.post(baseAPIurl + '/channel/user-list', data=data)
        return channelUserListHandler(**result.json())
    
    @staticmethod
    async def moveUser(
        target_id: str,
        user_ids: List[str]
    ) -> channelMoveUserHandler:
        """
        语音频道之间移动用户

        :param target_id: 语音频道ID
        :param user_ids: 需要移动用户的列表

        :return: channelMoveUserHandler
        """
        data = {
            "target_id": target_id,
            "user_ids": user_ids
        }
        result = await BotClient.post(baseAPIurl + '/channel/move-user', data=data)
        return channelMoveUserHandler(**result.json())

    class channelRole:
        @staticmethod
        async def index(
            channel_id: str
        ) -> channel_role.channelRoleIndexHandler:
            """
            频道角色权限详情

            :param channel_id: 频道ID

            :return: channelRoleIndexHandler
            """
            data = {
                "channel_id": channel_id
            }
            result = await BotClient.get(baseAPIurl + '/channel-role/index', params=data)
            return channel_role.channelRoleIndexHandler(**result.json())

        @staticmethod
        async def create(
            channel_id: str,
            type: Optional[str] == None,
            vaule: Optional[str] == None
        ) -> channel_role.channelRoleCreateHandler:
            """
            创建频道角色权限

            :param channel_id: 频道 id, 如果频道是分组的 id, 会同步给所有 sync=1 的子频道
            :param type: (可选)value 的类型, 只能为"role_id","user_id",不传则默认为"user_id"
            :param vaule: (可选)根据 type 的值, 为 用户 id 或 角色 id

            :return: channelRoleCreateHandler
            """
            if type not in ["role_id", "user_id"]:
                raise channelVauleError('不支持的类型')
            data = {
                "channel_id": channel_id,
                "type": type,
                "vaule": vaule
            }
            result = await BotClient.post(baseAPIurl + '/channel-role/create', data=data)
            return channel_role.channelRoleCreateHandler(**result.json())

        @staticmethod
        async def update(
            channel_id: str,
            type: Optional[str] == None,
            vaule: Optional[str] == None,
            allow: Optional[int] == None,
            deny: Optional[int] == None
        ) -> channel_role.channelRoleUpdateHandler:
            """
            编辑频道角色权限

            :param channel_id: 频道 id, 如果频道是分组的 id, 会同步给所有 sync=1 的子频道
            :param type: (可选)value 的类型, 只能为"role_id","user_id",不传则默认为"user_id"
            :param vaule: (可选)根据 type 的值, 为 用户 id 或 角色 id
            :param allow: (可选)默认为 0, 想要设置的允许的权限值
            :param deny: (可选)默认为 0,想要设置的拒绝的权限值

            :return: channelRoleUpdateHandler
            """
            if type not in ["role_id", "user_id"]:
                raise channelVauleError('不支持的类型')
            data = {
                "channel_id": channel_id,
                "type": type,
                "vaule": vaule,
                "allow": allow,
                "deny": deny
            }
            result = await BotClient.post(baseAPIurl + '/channel-role/update', data=data)
            return channel_role.channelRoleUpdateHandler(**result.json())

        @staticmethod
        async def sync(
            channel_id: str
        ) -> channel_role.channelRoleSyncHandler:
            """
            同步频道角色权限

            :param channel_id: 频道ID

            :return: channelRoleSyncHandler
            """
            data = {
                "channel_id": channel_id
            }
            result = await BotClient.get(baseAPIurl + '/channel-role/sync', params=data)
            return channel_role.channelRoleSyncHandler(**result.json())    

        @staticmethod
        async def create(
            channel_id: str,
            type: Optional[str] == None,
            vaule: Optional[str] == None
        ) -> channel_role.channelRoleDeleteHandler:
            """
            删除频道角色权限

            :param channel_id: 频道 id, 如果频道是分组的 id, 会同步给所有 sync=1 的子频道
            :param type: (可选)value 的类型, 只能为"role_id","user_id",不传则默认为"user_id"
            :param vaule: (可选)根据 type 的值, 为 用户 id 或 角色 id

            :return: channelRoleDeleteHandler
            """
            if type not in ["role_id", "user_id"]:
                raise channelVauleError('不支持的类型')
            data = {
                "channel_id": channel_id,
                "type": type,
                "vaule": vaule
            }
            result = await BotClient.post(baseAPIurl + '/channel-role/delete', data=data)
            return channel_role.channelRoleDeleteHandler(**result.json())
