from django.urls import path
from . import views

urlpatterns = [
    ## for this url call the index method of views class 
    path('', views.index,name="index")
]
