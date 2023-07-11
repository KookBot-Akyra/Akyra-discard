from typing import Optional

from .. import BotClient, baseAPIurl
from ...schema.Intimacy import intimacyHandler


class getIntimacyList:
    """
    好感度相关接口
    :Params: user_id: 用户ID
    :return: Intimacy.intimacy
    """

    @staticmethod
    async def list(user_id: str) -> intimacyHandler:
        data = {
            "user_id": user_id
        }
        result = await BotClient.get(url=baseAPIurl + "/intimacy/index", params=data)
        return intimacyHandler(**result.json())


class updateIntimacyList:
    """
    更新用户亲密度
    :Params: user_id
    :Params: score
    :Params: social_info
    :Params: img_id
    :return: Intimacy.updateIntimacyHandler
    """

    @staticmethod
    async def list(user_id: str, score: Optional[int] = None, social_info: Optional[str] = None,
                   img_id: Optional[str] = None) -> intimacyHandler:
        data = {
            "user_id": user_id,
            "score": score,
            "social_info": social_info,
            "img_id": img_id
        }
        result = await BotClient.post(url=baseAPIurl + "/intimacy/update", data=data)
        return intimacyHandler(**result.json())
