from django.contrib import admin
from django.urls import path

from .views import AddPet , DetailView , PetFilter , PetsView

urlpatterns = [
    path('' , PetsView , name = 'sahiplendirme'),
    path('ekle' , AddPet , name = 'ekle'),

    path('pets/<id>', DetailView , name='petsdetail'),
    path('filter/<kind>', PetFilter , name='petsfilter'),
]
