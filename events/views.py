from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event

def index(request):
    events_list = Event.objects.all()
    context = {'event_list': events_list}
    return render(request, 'events/events.html', context)
