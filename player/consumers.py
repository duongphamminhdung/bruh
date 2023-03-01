from channels.generic.websocket import JsonWebsocketConsumer
from .models import Room

import json

used_room_id = []
for room in Room.objects.all():
	used_room_id.append(room.room_id)

class PlayerConsumer(JsonWebsocketConsumer):
    

    def connect(self):
        self.room_id = int(self.scope['url_route']['kwargs']['room_id'])
        created_id = [i['room_id'] for i in Room.objects.values('room_id')]
        if self.room_id not in created_id:
            self.close()
            print("id not created")
        else:
            self.accept()
            print("connected", self.channel_name, "to group", self.room_id)
            self.channel_layer.group_add(str(self.room_id), self.channel_name)        
        return
    
    def receive_json(self, content):
        print(self.room_id, "receive", content)
        
        self.send_json("test")
        print("sent response", self.room_id)
        return
    def disconnect(self, close_code):
        self.channel_layer.group_discard("users", self.channel_name)
        print(f"Remove {self.room_id} channel from users's group")
        return
    
