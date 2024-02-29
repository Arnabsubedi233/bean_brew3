from django.shortcuts import redirect,render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User





# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Hey {username}, your account was created successfully!")
            new_user = authenticate(username = form.cleaned_data['email'],
                                    password= form.cleaned_data['password1'])
            login(request,new_user)
            return redirect("home:index")
    else:
        form = UserRegisterForm()
        

    context = {
        'form': form,
    }
    return render(request,"userauths/register.html",context)

def LoginView(request):
    if request.user.is_authenticated:
        return redirect("home:index")
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
            user = authenticate(request,email=email,password = password)
        
            if user is not None:
                login(request,user)
                messages.success(request,f"You are logged in!")
                return redirect("home:index")
            else:
                messages.warning(request,f'User does not exist!,Create an account')
        except:
            messages.warning(request,f'User with {email} does not exist!')

       
            
        
    return render(request,"userauths/login.html")

def LogoutView(request):
    logout(request)
    messages.warning(request,f'You successfully logged out!')
    return redirect("userauths:login")





