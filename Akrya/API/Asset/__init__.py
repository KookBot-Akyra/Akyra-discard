from .. import BotClient, baseAPIurl
from ...schema.Asset import *
from typing import Union

class asset:
    """
    媒体模块接口
    """
    @staticmethod
    async def create(file: Union[str, bytes]):
        """
        上传媒体文件
        
        :param file: str/bytes类型, 需要上传的文件(只能单个)
        :return: create 
        """
        body = {
            "file": file
        }
        result = await BotClient.post(baseAPIurl + '/asset/create', data=body)
        return create(**result.json())
