from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView, name='index')
]
