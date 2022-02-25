from django.urls import path
from . import views

urlpatterns = [
    path('', views.preciosL, name='preciosL')
]

