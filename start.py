from Akrya.main import run_ws_client
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(run_ws_client())