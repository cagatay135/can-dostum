from django.contrib import admin
from django.urls import path

from .views import BlogListView , BlogDetailView , BlogTagView

urlpatterns = [
    path('' , BlogListView , name = 'blog'),
    path('<int:pk>/' , BlogDetailView , name='blog_detail'),
    path('tag/<str:tag>/' , BlogTagView , name = 'tag'),
]
