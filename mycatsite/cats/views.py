from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'cats/index.html')

def breeds(request):
    return render(request, 'cats/breeds.html')

def gallery(request):
    return render(request, 'cats/gallery.html')

def contacts(request):
    return render(request, 'cats/contacts.html')