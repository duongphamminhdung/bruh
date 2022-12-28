from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'api/<int:room_id>/', consumers.PlayerConsumer.as_asgi()),
]
