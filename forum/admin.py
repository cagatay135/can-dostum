from django.contrib import admin

from . models import ForumPost , ForumComments

# Register your models here.
admin.site.register(ForumPost)
admin.site.register(ForumComments)