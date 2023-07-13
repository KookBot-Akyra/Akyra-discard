import time
import zlib
import json
import asyncio

from abc import ABC, abstractmethod
from aiohttp import ClientWebSocketResponse, ClientSession, web, WSMessage

from .log import logger
from .config import ws_compress
from .schema.wsHandler import EventHandler
from .API.Gateway import gateway
from .interface import AsyncRunnable

__name__ = 'WebSocket'

class Receiver(AsyncRunnable, ABC):
    """
    1. receive raw data from khl server
    2. decrypt & parse raw data into pkg
    3. put pkg into the pkg_queue() for others to use
    """
    _queue: asyncio.Queue

    @property
    def type(self) -> str:
        """the network type used by the receiver"""
        raise NotImplementedError

    @property
    def pkg_queue(self) -> asyncio.Queue:
        """output port of the receiver"""
        return self._queue

    @pkg_queue.setter
    def pkg_queue(self, queue: asyncio.Queue):
        self._queue = queue

    @abstractmethod
    async def start(self):
        """run self"""
        raise NotImplementedError

async def GetWssUrl():
    result = await gateway.index(0)
    logger.info("尝试获取WsUrl")
    return result.data.url

class Websocket_Connetion(Receiver):
    """
    Websocket连接类
    """
    sn: int = 0
    s: int = -1
    session_id: str = ""

    def __init__(self):
        super().__init__()

    async def heartbeat(self, ws_conn: ClientWebSocketResponse):
        """khl customized heartbeat scheme"""
        while True:
            try:
                await asyncio.sleep(26)
                await ws_conn.send_json({'s': 2, 'sn': self.sn})
            except ConnectionResetError:
                return
            except Exception as e:
                logger.exception('error raised during websocket heartbeat', exc_info=e)

    async def _connect_gateway_and_handle_msg(self, cs: ClientSession):
        async with cs.ws_connect(self.wsurl) as ws_conn:
            self.ping_task = asyncio.ensure_future(self.heartbeat(ws_conn), loop=self.loop)
            logger.info('[ init ] 连接已启动')
            try:
                async for raw in ws_conn:
                    raw: WSMessage
                    await self.MessageHandler(raw.data, True if ws_compress == 1 else False)
            except Exception:
                logger.exception(
                    'error raised during websocket receive, reconnect automatically'
                )

    async def start(self):
        """
        requires:
            wsurl: kook wss Url
        """
        wsurl = await GetWssUrl()
        self.wsurl = wsurl
        async with ClientSession(loop=self.loop) as cs:
            while True:
                await self._connect_gateway_and_handle_msg(cs)

    async def MessageHandler(self, message: str, compress: bool):
        # 信息处理
        result = EventHandler(**json.loads(str(zlib.decompress(message), 'utf-8'))) if compress else EventHandler(**json.loads(str(message)))
        self.s = result.s
        data = result.d
        if self.s == 1 or self.s == 6:
            if data.code == 0:
                self.session_id = data.session_id
        elif self.s == 0:
            self.sn = result.sn
            channel_type = data.channel_type # 消息通道类型
            # 你丫的kook不TM统一一下类型，一会TM 字符串一会整数型, 有病
            type = int(data.type) # 消息类型
            if type == 255:
                return
            user_name = data.extra.author.username # 用户名
            identify_num = data.extra.author.identify_num # 用户名的认证数字
            guild_id = data.extra.guild_id # 服务器ID
            content = data.content # 消息内容
            msg_id = data.msg_id # 消息ID
            msg_timestamp = time.strftime("%m-%d %H:%M:%S", time.localtime(data.msg_timestamp / 1000)) # 发送时间
            msg = f"{msg_timestamp} 服务器({guild_id})接收到消息: 通道类型: {channel_type}, 消息类型: {type}, 发送者: {user_name}#{identify_num}, 内容: \"{content}\" - {msg_id}"
            logger.info(msg)