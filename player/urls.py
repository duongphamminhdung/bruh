from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("createID/", views.create_room_id, name="create-room"),
    path("deleteID/<int:room_id>", views.delete_room_id, name="delete-room"),
    path("connect/<int:room_id>/", views.connect_room_id, name="Connect")
]