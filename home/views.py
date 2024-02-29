from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"home/homepage.html")

def store(request):
    return render(request,'Store/services.html')

def about(request):
    return render(request,'about/About.html')