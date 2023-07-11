from .API.Gateway import gateway
from .log import logger
from .config import ws_compress
from .websocket import Websocket_Connetion

__name__ = 'Akrya'

async def getWssUrl() -> str:
    """
    用于获取连接Kook的Wss地址
    """

    result = await gateway.index(ws_compress)
    url = result.data.url
    logger.info('获取到WsUrl, 尝试连接')
    return url

async def run_ws_client():
    client = Websocket_Connetion()
    await client.run(await getWssUrl(), False)
