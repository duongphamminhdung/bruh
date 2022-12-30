from channels.generic.websocket import WebsocketConsumer
import json

class PlayerConsumer(WebsocketConsumer):
    
    def __init__(self):
        room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_id = room_id
        print(room_id)

    def connect(self):
        self.accept()
        print("connected")
        
        return
    def receive(self, text_data=None, bytes_data=None):
        print("receive")
        return super().receive(text_data)
