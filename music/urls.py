from django.urls import path
from music import views

app_name = 'music'
urlpatterns = [
    path('', views.IndexView, name='index'),
]