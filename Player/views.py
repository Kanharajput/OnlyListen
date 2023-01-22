from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def playAudio(request):
    return HttpResponse("<h1> Playing your audio </h1>")