from django.urls import path
from . import views

urlpatterns = [
    path('',views.playAudio)           # url = localhost/listen
]
