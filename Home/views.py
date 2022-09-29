from distutils.command.upload import upload
from pathlib import Path
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
import pdfplumber
import pyttsx3 

# Create your views here.
def index(request):
    page_no = 1
    ## initialize the pyttsx3 object
    engine =  initializeEngine()
    
    if(request.method =="POST"):
        uploaded_file = request.FILES['document']

        ## open the file to read 
        with pdfplumber.open(uploaded_file) as pdf:

            # getting name of the file without extension
            file_name = 'static/upload/%s' % uploaded_file
            file_name = Path(file_name).stem

            for page in pdf.pages:
                content = page.extract_text()
                print(content)
                engine.save_to_file(content,"static/upload/"+file_name+str(page_no)+".mp3")
                engine.runAndWait()
                ## there are no increment decrement operator in python 
                page_no = page_no + 1

    return render(request,'index.html')

## initializing the engine
def initializeEngine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    ## get thee voice of Hazel
    voice = voices[3]
    engine.setProperty('voice',voice.id)
    return engine
