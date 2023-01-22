from django.shortcuts import render

# Create your views here.
def playAudio(request):
    return render(request,"Player/player.html")