from django.urls import path
from .views import category
urlpatterns = [
    path('',category,name='category'),
]