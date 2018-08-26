from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from events.models import Registrations

def index(request):
    context = {}
    return render(request, 'register/register.html', context)
