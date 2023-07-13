from .log import logger
from .config import ws_compress
from .websocket import Websocket_Connetion
from .interface import AsyncRunnable

from typing import List, Callable, Coroutine

import asyncio

__name__ = 'Akrya'

TypeShutdownHandler = Callable[['Run'], Coroutine]

class Run(AsyncRunnable):
    _shutdown_index: List[TypeShutdownHandler]

    def __init__(self) -> None:
        self._shutdown_index = []

    def on_shutdown(self, func: TypeShutdownHandler):
        """decorator, register a function to handle bot stop"""

        self._shutdown_index.append(func)

        return func

    def start(self):
        try:
            self.client = Websocket_Connetion()
            if self.loop:
                self.loop.run_until_complete(self.client.start())
            else: 
                self.loop = asyncio.new_event_loop()
                self.loop.run_until_complete(self.client.start())
        except KeyboardInterrupt:
            logger.info('see you next time')
