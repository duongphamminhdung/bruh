from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)
from channels.generic.websocket import WebsocketConsumer
import json

class PlayerConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("connected")
        
        return
    def receive(self, text_data=None, bytes_data=None):
        print("receive")
        return super().receive(text_data, bytes_data)
