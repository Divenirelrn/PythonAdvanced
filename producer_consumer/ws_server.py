#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: lu zhao
# Python 3.6.7

import asyncio
import websockets
from multiprocessing import Queue, Lock
import json
#初始化队列与锁
q = Queue()
lock = Lock()

def data_put(data):
    if q.full():
        return

    lock.acquire()
    q.put(data)
    lock.release()
    print("data putted")


async def producer_handler(websocket, path):
    print('---- websocket已连接 -----')

    while True:
        #fetch data
        if q.empty():
            #print("q is empty")
            continue
        lock.acquire()
        data = q.get()
        lock.release()
        print("data getted")
        print("data:", data)
        #send data
        await websocket.send(json.dumps(data))
        print("send done")
        #result = await websocket.recv()
        #print(result)


def wb_svr_start():
    start_server = websockets.serve(producer_handler, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    wb_svr_start()
