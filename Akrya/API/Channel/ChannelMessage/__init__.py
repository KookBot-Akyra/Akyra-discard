from ....schema.Channel.ChannelMessage import *
from ...import baseAPIurl, BotClient

from typing import Optional
from urllib.parse import urlencode

class channelMessage():
    "频道消息相关接口"

    @staticmethod
    async def list(
        target_id: str, 
        msg_id: Optional[str] = None, 
        pin: Optional[int] = 0, 
        flag: Optional[str] = None, 
        page_size: Optional[int] = 50
    ) -> channelMessageListHandler:
        """
        获取频道聊天消息列表

        :param target_id: 频道 id
        :param msg_id: 频道消息 id, 不传则查询最新消息
        :param pin: 只能为 0 或者 1, 是否查询置顶消息. 置顶消息只支持查询最新的消息
        :param flag: 查询模式, 有三种模式可以选择. 不传则默认查询最新的消息
            //before 查询参考消息之前的消息, 不包括参考消息. 

            //around 查询以参考消息为中心, 前后一定数量的消息. 

            //after 查询参考消息之后的消息, 不包括参考消息. 
        :param page_size: 当前分页消息数量, 默认 50

        :return: channelMessageListHandler
        """
        data = {
            "target_id": target_id,
            "msg_id": msg_id,
            "pin": pin,
            "flag": flag,
            "page_size": page_size
        }
        result = await BotClient.get(baseAPIurl + '/message/list', params=data)
        return channelMessageListHandler(**result.json())
    
    @staticmethod
    async def view(
        msg_id: str
    ) -> channelMessageViewHandler:
        """
        获取频道聊天消息详情

        :param msg_id: 频道消息ID

        :return: channelMessageViewHandler
        """
        data = {
            "msg_id": msg_id
        }
        result = await BotClient.get(baseAPIurl + '/message/view', params=data)
        return channelMessageViewHandler(**result.json())

    @staticmethod
    async def create(
        type: Optional[int], 
        target_id: str, 
        content: str, 
        quote_msg_id: Optional[str], 
        nonce: Optional[str], 
        temp_target_id: Optional[str]
    ) -> channelMessageCreateHandler:
        """
        发送频道聊天消息

        :param type: 消息类型, 见[type], 不传默认为 1, 代表文本类型. 9 代表 kmarkdown 消息, 10 代表卡片消息. 
        :param target_id: 目标频道 id
        :param content: POST频道消息内容
        :param quote_msg_id: 回复某条消息的 msgId
        :param nonce: 该项服务端不做处理, 原样返回
        :param temp_target_id: 用户 id, 如果传了, 代表该消息是临时消息, 该消息不会存数据库, 但是会在频道内只给该用户推送临时消息. 用于在频道内针对用户的操作进行单独的回应通知等. 

        :return: channelMessageCreateHandler
        """
        data = {
            "type": type,
            "target_id": target_id,
            "content": content,
            "quote": quote_msg_id,
            "nonce": nonce,
            "temp_target_id": temp_target_id
        }
        result = await BotClient.post(baseAPIurl + '/message/create', data=data)
        return channelMessageCreateHandler(**result.json())

    @staticmethod
    async def update(
        msg_id: str, 
        content: str, 
        quote_msg_id: Optional[str], 
        temp_target_id: Optional[str]
    ) -> channelMessageUpdateHandler:
        """
        更新频道聊天消息

        目前支持消息 type 为 9, 10 的修改, 即 KMarkdown 和 CardMessage

        :param msg_id: 频道消息ID
        :param content: 更改的消息内容
        :param quote_msg_id: 回复某条消息的 msgId. 如果为空, 则代表删除回复, 不传则无影响. 
        :param temp_target_id: 用户 id, 针对特定用户临时更新消息, 必须是正常消息才能更新. 与发送临时消息概念不同, 但同样不保存数据库. 

        :return: channelMessageUpdateHandler
        """
        data = {
            "msg_id": msg_id,
            "content": content,
            "quote": quote_msg_id,
            "temp_target_id": temp_target_id
        }
        result = await BotClient.post(baseAPIurl + '/message/update', data=data)
        return channelMessageUpdateHandler(**result.json())

    @staticmethod
    async def delete(
        msg_id: str
    ) -> channelMessageDeleteHandler:
        """
        删除频道聊天消息
        
        :param msg_id: 需要删除的频道消息ID

        :return: channelMessageDeleteHandler
        """
        data ={
            "msg_id": msg_id
        }
        result = await BotClient.post(baseAPIurl + '/message/delete', data=data)
        return channelMessageDeleteHandler(**result.json())

    @staticmethod
    async def reaction_list(
        msg_id: str, 
        emoji: str
    ) -> channelMessageReactionListHandler:
        """
        获取频道消息某回应的用户列表

        :param msg_id: 频道消息的 id
        :param emoji: emoji 的 id, 可以为 GuilEmoji 或者 Emoji

        :return: channelMessageReactionListHandler
        """
        data = {
            "msg_id": msg_id,
            "emoji": emoji
        }
        result = await BotClient.get(baseAPIurl + '/message/reaction-list?' + urlencode(data))
        return channelMessageReactionListHandler(**result.json())

    @staticmethod
    async def add_reaction(
        msg_id: str, 
        emoji: str
    ) -> channelMessageAddReactionHandler:
        """
        给某个消息添加回应

        :param msg_id: 频道消息的 id
        :param emoji: emoji 的 id, 可以为 GuilEmoji 或者 Emoji

        :return: channelMessageAddReactionHandler
        """
        data = {
            "msg_id": msg_id,
            "emoji": emoji
        }
        result = await BotClient.post(baseAPIurl + '/message/add-reaction', data=data)
        return channelMessageAddReactionHandler(**result.json())
    
    @staticmethod
    async def delete_reaction(
        msg_id: str, 
        emoji: str, 
        user_id: Optional[str] = None
    ) -> channelMessageDeleteReactionHandler:
        """
        给某个消息添加回应

        :param msg_id: 频道消息的 id
        :param emoji: emoji 的 id, 可以为 GuilEmoji 或者 Emoji
        :param user_id: 用户的 id, 如果不填则为自己的 id. 删除别人的 reaction 需要有管理频道消息的权限.
        """
        data = {
            "msg_id": msg_id,
            "emoji": emoji,
            "user_id": user_id            
        }
        result = await BotClient.post(baseAPIurl + '/message/delete-reaction', data=data)
        return channelMessageDeleteReactionHandler(**result.json())
