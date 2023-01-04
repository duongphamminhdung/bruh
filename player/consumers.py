from channels.generic.websocket import WebsocketConsumer
import json

class PlayerConsumer(WebsocketConsumer):
    

    def connect(self):
        self.accept()
        print("connected")
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        print(self.room_id)
        
        return
    def receive(self, text_data=None, bytes_data=None):
        print(self.room_id, "receive", text_data)
        return super().receive(text_data)
