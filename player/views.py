from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Player

def index(request):
    template = loader.get_template('index.html')

    return HttpResponse(template)
