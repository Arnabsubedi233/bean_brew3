from django.shortcuts import render
from django.http import HttpResponse
from .models import reservation
from .forms import ReserveTableForm

# Create your views here.
def index(request):
    return render(request,"home/homepage.html")



def about(request):
    return render(request,'about/About.html')

def store(request):
    return render(request,'Store/services.html')

