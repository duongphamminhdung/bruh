from channels.generic.websockets import WebsocketConsumer
import json

class PlayerConsumer(WebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("connected")
        
        return
    async def receive(self, text_data=None, bytes_data=None):
        print("receive")
        await self.send("received")
