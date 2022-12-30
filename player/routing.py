from django.urls import path, re_path

from player import consumers

websocket_urlpatterns = [
    re_path(r'ws/connect/', consumers.PlayerConsumer.as_asgi()),
]
