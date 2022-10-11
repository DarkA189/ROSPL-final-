from django.http import HttpResponse
from django.shortcuts import render
import pywhatkit as kit
import cv2




def index(request):
    return render(request, 'home.html')


def texthand(request):
    return render(request, 'texthand.html')

def processHandtoText(request):
    if request.method == "POST":
        content = request.POST.get('content-area')
        
        kit.text_to_handwriting(content, save_to="static/images/handwriting.png")
        return render(request,'texthandresults.html')


