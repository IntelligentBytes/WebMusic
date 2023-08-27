from django.urls import path
from album import views

app_name = 'album'
urlpatterns = [
    path("",views.IndexView,name="index")
]