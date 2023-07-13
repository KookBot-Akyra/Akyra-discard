import asyncio
from abc import ABC, abstractmethod


class AsyncRunnable(ABC):
    """
    Classes that has async work to run
    """
    _loop: asyncio.AbstractEventLoop = None

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        """the event loop for the async work"""
        return self._loop

    @loop.setter
    def loop(self, new_loop: asyncio.AbstractEventLoop):
        self._loop = new_loop

    def schedule(self):
        """schedule the async work into background"""
        asyncio.ensure_future(self.start(), loop=self.loop)

    @abstractmethod
    async def start(self):
        """run the async work"""