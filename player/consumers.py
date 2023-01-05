from channels.generic.websocket import WebsocketConsumer
from .models import Room

import json

used_room_id = []
for room in Room.objects.all():
	used_room_id.append(room.room_id)

class PlayerConsumer(WebsocketConsumer):
    

    def connect(self):
        self.room_id = int(self.scope['url_route']['kwargs']['room_id'])
        created_id = [i['room_id'] for i in Room.objects.values('room_id')]
        if self.room_id not in created_id:
            self.close()
            print("id not created")
        else:
            self.accept()
            print("connected")
        print(self.room_id)
        
        return
    def receive(self, text_data=None, bytes_data=None):
        print(self.room_id, "receive", text_data)
        return super().receive(text_data)
