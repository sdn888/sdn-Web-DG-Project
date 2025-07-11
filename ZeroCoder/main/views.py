from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html', {'caption':"MyDjango"})
def new(request):
    return render(request, 'main/new.html')
def project(request):
    return render(request, 'main/project.html')
def contact(request):
    return render(request, 'main/contact.html')



