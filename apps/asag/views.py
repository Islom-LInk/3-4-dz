from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    Settings = Settings.objects.latest('id',locals()) 
    return render(request, 'index.html')

def contact(request):
    Settings = Settings.objects.latest('id') 
    return render(request, 'contact.html')

def index(request):
    return HttpResponse("Главная страница")

