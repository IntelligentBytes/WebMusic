from django.urls import path
from album import views

app_name = 'category'
urlpatterns = [
    path("",views.IndexView,name="index")
]