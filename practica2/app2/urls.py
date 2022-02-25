
from re import A
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar', views.agregar, name='agregar'),
    
]