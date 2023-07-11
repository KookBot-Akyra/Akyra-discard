from .. import BotClient, baseAPIurl
from ...schema.Gateway import gatewayHandler

class gateway:

    @staticmethod
    async def index(compress: int = 1) -> gatewayHandler:
        """
        requires:
            compress: 下发数据是否压缩, 默认为 '1' 代表压缩

        return:
            gatewayHandler
        """
        data = {
            "compress": compress
        }
        result = await BotClient.get(url=baseAPIurl + "/gateway/index", params=data)
        return gatewayHandler(**result.json())