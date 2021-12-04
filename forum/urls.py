from django.contrib import admin
from django.urls import path

from .views import ForumView , ForumDetailView , ForumTagView , AddForumPost

urlpatterns = [
    path('' , ForumView , name = 'forum'),
    path('<int:pk>/' , ForumDetailView , name='forum_detail'),
    path('tag/<str:tag>/' , ForumTagView , name = 'forum_tag'),
    path('ekle/' , AddForumPost , name = 'add_forum_post'),

]
