import websocket
import threading
import time

def on_message(ws, message):
    print("Recieve:", message)

def on_open(ws):
    def send():
        for i in range(5):
            time.sleep(0.1)
            ws.send(f"{i}")
            print("Send:", i)
        time.sleep(1)

        ws.close()
        print("websocket closed")

    threading.Thread(target=send).start()

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:10000", on_message=on_message, on_open=on_open)

    ws.run_forever()
