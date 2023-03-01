# from websocket import create_connection as C
import websocket
import json

# url = 'ws://192.168.1.16:8000/ws/connect/200'
url = 'ws://127.0.0.1:8000/ws/connect/100'
# ws = C(url)
content = {
    'p1':{'x':127,
        'y':140,
        'money':12764,},
    'p2':{'x':129,
        'y':40,
        'money':23441
    }
}


def on_open(ws):
    ws.send(json.dumps({"text":"Connected to server"}))
    
def on_message(ws, message):
    print("message")

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever(reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
