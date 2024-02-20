from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("login-sign-up/",views.register_view,name= 'login-sign-up')
]