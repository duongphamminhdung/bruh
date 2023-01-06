from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Player, Room, lst
from django.shortcuts import  render, redirect
from django.contrib import messages
import random
from create_socket import run_socket
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
	prev = 0
	for room in Room.objects.all():
		if room.order != prev+1:
			temp = room.order
			room.order = prev+1
			Room.objects.get(order=temp).delete()
		prev += 1
		room.save()
	context = {}
	print(used_room_id)
	return render(request=request, template_name="index.html", context=context)

room_id_not_used = lst([i for i in range(100, 1000)])
used_room_id = []
random.shuffle(room_id_not_used)
for room in Room.objects.all():
	room_id_not_used.remove(room.room_id)
	used_room_id.append(room.room_id)
 
@csrf_protect
def create_room_id(request):
	room = Room(room_id=room_id_not_used[0])
	used_room_id.append(room_id_not_used[0])
	room_id_not_used.pop(0)
	All = Room.objects.all()
	room.order = len(All)+1
	room.save()
	print(used_room_id)
	return render(request=request, template_name="createID.html", context={"room_id":room.room_id})
 
@csrf_protect
def delete_room_id(request, room_id):
	room = Room.objects.get(room_id=room_id)
	room_id_not_used.append(room_id)
	used_room_id.remove(room_id)
	room.delete()
	return render(request=request, template_name="index.html", context={})
 
