from distutils.command.upload import upload
from pathlib import Path
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.shortcuts import render
from gtts import gTTS
import pdfplumber
#import pyttsx3 

# Create your views here.
def index(request):
    page_no = 1
    # Language in which you want to convert
    language = 'en'
    
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
                # change library to gtts as pyttsx3 is depend on system speakers 
                # later in future we have to change gTTS also due to it's slow operational speed
                audioData = gTTS(text=content, lang=language, slow=False)

                audioData.save("static/upload/"+file_name+str(page_no)+".mp3")
                ## there are no increment decrement operator in python 
                page_no = page_no + 1

    return render(request,'Home/index.html')