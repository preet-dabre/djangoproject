from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import About_models


def index(request):
    context = None
    return render(request, 'about/about.html', context)
