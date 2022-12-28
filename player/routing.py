from django.urls import path, re_path

from . import consumers
from channels.generic.websockets import WebsocketDemultiplexer
from channels.routing import route_class
from consumers import consumers

websocket_urlpatterns = [
    path(r'connect/(?P<room_id>\w+)/$', consumers.PlayerConsumer.as_asgi()),
]
