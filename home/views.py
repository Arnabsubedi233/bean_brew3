from django.shortcuts import render
from django.http import HttpResponse
from .models import reservation
from .forms import ReserveTableForm
from home.models import reservation

# Create your views here.
def index(request):
    return render(request,"home/homepage.html")



def about(request):
    return render(request,'about/About.html')

def store(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form':reserve_form}
    return render(request,'Store/services.html',context)

