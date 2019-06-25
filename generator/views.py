from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SmashTag
import random

# Create your views here.
def index(request):
    #firstFive = SmashTag.objects.all()[:10]
    context = {
        #'firstFive': firstFive,
        'curTag': random.choice(SmashTag.objects.all()).tag,
    }
    return render(request, 'generator/index.html', context)

def detail(request, tag):
    return HttpResponse("Tag: " + tag)

def getTag(request):
    context = {
        'curTag': random.choice(SmashTag.objects.all()).tag,
    }
    return render(request, 'generator/index.html', context)