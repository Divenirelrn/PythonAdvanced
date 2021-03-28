import asyncio
import websockets

async def consumer_handler():
    async with websockets.connect('ws://localhost:8765') as websocket:
        async for message in websocket:
            websocket.send("i am fine")
            print(message)
                                                

asyncio.get_event_loop().run_until_complete(consumer_handler())
asyncio.get_event_loop().run_forever()
