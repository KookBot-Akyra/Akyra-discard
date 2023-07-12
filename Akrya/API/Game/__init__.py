from typing import Optional
from .. import baseAPIurl, BotClient
from ...schema.Game import *


class game:
    """
    游戏/进程/音乐
    """

    @staticmethod
    async def list(
        type: Optional[str] = None,
    ) -> gameHandlerBase:
        """
        获取游戏列表

        :param type: 游戏类型

        :return: gameHandlerBase
        """

        data = {
            "type": type
        }
        result = await BotClient.get(baseAPIurl + "/game", params=data)
        return gameHandlerBase(**result.json())

    @staticmethod
    async def create(name: str, icon: Optional[str] = None) -> gameHandlerBase:
        """
        获取游戏列表
        :param name: 游戏名称
        :param icon: 游戏图标
        单日最大可创建 5 个游戏数据！！

        :return: gameHandlerBase
        """

        data = {
            "name": name
        }
        if icon:
            data["icon"] = icon
        result = await BotClient.post(baseAPIurl + "/game/create", data=data)
        return gameHandlerBase(**result.json())

    @staticmethod
    async def update(
        id: int, name: Optional[str] = None, icon: Optional[str] = None
    ) -> gameHandlerBase:
        """
        更新游戏
        :param id: 游戏ID
        :param name: 游戏名称
        :param icon: 游戏图标
        :return gameHandlerBase

        """
        data = {
            "id": id
        }
        if name:
            data["name"] = name
        if icon:
            data["icon"] = icon
        result = await BotClient.post(baseAPIurl + "/game/update", data=data)
        return gameHandlerBase(**result.json())

    @staticmethod
    async def delete(id: int) -> gameHandlerBase:
        """
        删除游戏
        :param id: 游戏ID
        :return deleteHandler
        """
        data = {
            "id": id
        }
        result = await BotClient.post(baseAPIurl + "/game/delete", data=data)
        return gameHandlerBase(**result.json())

    @staticmethod
    async def activity(
        id: int,
        data_type: int,
        software: Optional[str] = None,
        singer: Optional[str] = None,
        music_name: Optional[str] = None,
    ) -> gameHandlerBase:
        """
        添加游戏/音乐记录-开始玩/听
        :param id: 游戏ID
        :param data_type: 数据类型
        :param software: 软件名称
        :param singer: 歌手
        :param music_name: 歌曲名称
        :return: gameHandlerBase
        """
        data = {
            "id": id, 
            "type": data_type
        }
        if software:
            data["software"] = software
        if singer:
            data["singer"] = singer
        if music_name:
            data["music_name"] = music_name
        result = await BotClient.post(baseAPIurl + "/game/activity", data=data)
        return gameHandlerBase(**result.json())

    @staticmethod
    async def activity_delete(data_type: int) -> gameHandlerBase:
        """
        删除游戏/音乐记录-结束玩/听
        :param data_type: 数据类型
        :return Game.gameHandlerBase

        """
        data = {
            "type": data_type
        }
        result = await BotClient.post(baseAPIurl + "/game/delete-activity", data=data)
        return gameHandlerBase(**result.json())
