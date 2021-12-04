from django.contrib import admin
from django.urls import path

from .views import AddLostPet

urlpatterns = [
    path('ekle' , AddLostPet , name = 'kayip'),
]
