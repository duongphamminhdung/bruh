from websocket import create_connection as C
import json

url = 'ws://127.0.0.1:8000/ws/connect/200'
ws = C(url)
content = {
    'p1':{'x':127,
        'y':140,
        'money':12764,},
    'p2':{'x':129,
          'y':40,
          'money':23441
    }
}
ws.send(json.dumps(content))
ws.recv()