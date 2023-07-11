from typing import Optional

from .. import BotClient, baseAPIurl
from ...schema.Intimacy import *

class intimacy:
    """
    亲密度相关接口
    """
    
    @staticmethod
    async def index(
        user_id: str
    ) -> intimacyIndexHandler:
        """
        获取用户亲密度

        :params user_id: 用户ID

        :return: Intimacy.intimacy
        """
        data = {
            "user_id": user_id
        }
        result = await BotClient.get(url=baseAPIurl + "/intimacy/index", params=data)
        return intimacyIndexHandler(**result.json())

    @staticmethod
    async def update(
        user_id: str, 
        score: Optional[int] = None, 
        social_info: Optional[str] = None,
        img_id: Optional[str] = None
    ) -> intimacyUpdateHandler:
        """
        更新用户亲密度

        :params user_id: 用户ID
        :params score: 
        :paramss ocial_info: 
        :params img_id: 

        :return: Intimacy.updateIntimacyHandler
        """
        data = {
            "user_id": user_id,
            "score": score,
            "social_info": social_info,
            "img_id": img_id
        }
        result = await BotClient.post(url=baseAPIurl + "/intimacy/update", data=data)
        return intimacyUpdateHandler(**result.json())
