from django.contrib import admin
from .models import Player, Room
# Register your models here.

@admin.register(Room)
class Room_admin(admin.ModelAdmin):
    list_display = ['order', 'room_id']