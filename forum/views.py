from django.shortcuts import render, redirect
# Create your views here.
from .forms import Comments 
from .forms import Posts 

from .models import ForumPost
from django.db.models import Q
def ForumView(request):

    search_query = request.GET.get('search' , '')
    if search_query:
        object_list = ForumPost.objects.all().filter(Q(title__icontains=search_query))
    else:
        object_list = ForumPost.objects.all().order_by('-created_date')

    return render(request, "forum.html" , {'object_list': object_list})


def ForumDetailView(request , pk):
    post = ForumPost.objects.get(pk=pk)
    if request.method == "POST":
        form = Comments(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post = ForumPost.objects.get(pk=pk)
            post.save()
            return redirect('forum_detail' , pk=pk)

    else:
        form = Comments()
    return render(request, "forum_detail.html", {'post': post , 'form' : form} )

def ForumTagView(request, tag):
    object_list = ForumPost.objects.filter(tag=tag)

    return render(request, 'forum.html', {'object_list' : object_list})

def AddForumPost(request):
    if request.method == "POST":
        form = Posts(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum_detail', pk=post.pk)

    else:
        form = Posts()

    return render(request, 'add_forum_post.html', {'form' : form})
