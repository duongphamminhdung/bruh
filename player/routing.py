from django.urls import path, re_path

from player import consumers
from channels import route, route_class

channel_routing = [
    route_class(consumers.PlayerConsumer, path=r"^/ws/connect"),
    route("websocket.connect", consumers.ws_connect, path=r"^/$"),
]
websocket_urlpatterns = [
    re_path(r'ws/connect/', consumers.PlayerConsumer.as_asgi()),
]
