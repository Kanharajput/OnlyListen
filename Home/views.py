from distutils.command.upload import upload
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
import pdfplumber
import pyttsx3 

# Create your views here.
def index(request):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice = voices[2]
    engine.setProperty('voice',voice.id)
    
    if(request.method =="POST"):
        uploaded_file = request.FILES['document']
        with pdfplumber.open(uploaded_file) as pdf:
            page = pdf.pages[0]
            content = page.extract_text()
            print(content)
            engine.save_to_file(content,"static/upload/Trial.mp3")
            engine.runAndWait()

    return render(request,'index.html')