import websocket
import time
import zlib
import json
import random
import rel
import asyncio
import threading

from .log import logger
from .config import ws_compress
from .schema.wsHandler import EventHandler

__name__ = 'WebSocket'

class Websocket_Connetion:
    """
    Websocket连接类
    """
    sn: int = 0
    s: int = -1
    session_id: str = ""
    url: str = "wss://"

    def __init__(self):
        pass

    async def run(self, wsurl: str, is_reconnect: bool):
        """
        requires:
            wsurl: kook wss Url
        """
        if is_reconnect:
            wsurl = wsurl + '&resume=1&sn=5&session_id=' + self.session_id
            self.sn = 0
            self.s = -1
            self.session_id = ""
        self.wsurl = wsurl
        self.ws = websocket.WebSocketApp(
            wsurl,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_ping=self.on_ping,
            on_pong=self.on_pong
        )
        self.ws.run_forever(dispatcher=rel, ping_interval=30 + random.randint(-5, 5), ping_timeout=6)
        self.ws.ping_payload = json.dumps({"s":2, "sn": self.sn})
        rel.signal(2, rel.abort)
        rel.dispatch()

    def on_ping(wsapp, ws, message):
        pass

    def on_pong(wsapp, ws, message):
        pass

    def on_message(self, ws, message):
        def handler(message):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            if ws_compress == 1:
                loop.run_until_complete(self.MessageHandler(message, True))
            elif ws_compress == 0:
                loop.run_until_complete(self.MessageHandler(message, False))

        threading.Thread(target=handler, args=(message, )).start()

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
            self.ws.ping_payload = json.dumps({"s":2, "sn": self.sn})
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

    def on_error(self, ws, error):
        logger.error(error)

    def on_close(self, ws, close_status_code, close_msg):
        logger.info("连接已关闭")

    def on_open(self, ws):
        logger.info("连接已开启")