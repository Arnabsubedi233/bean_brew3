from django.urls import path
from home.views  import index
from home.views import store

app_name = "home"

urlpatterns = [
    path("",index,name = "index"),
    path('store/',store,name='store')
]
