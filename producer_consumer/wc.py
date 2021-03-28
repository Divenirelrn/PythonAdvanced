import websocket


def on_message(ws, message):
    print(ws)
    print(message)


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")

def on_open(ws):
    ws.send("hello server")

websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://127.0.0.1:8765",
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.on_open = on_open

ws.run_forever()
