from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
from .forms import Comments 
from .models import Post
from django.db.models import Q

def BlogListView(request):
    search_query = request.GET.get('search' , '')
    if search_query:
        object_list = Post.objects.all().filter(Q(text__icontains=search_query))
    else:
        object_list = Post.objects.all().order_by('-created_date')

    return render(request, "blog.html", {'object_list': object_list})

def BlogDetailView(request , pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = Comments(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post = Post.objects.get(pk=pk)
            post.save()
            return redirect('blog')

    else:
        form = Comments()
    return render(request, "blog_detail.html", {'post': post , 'form' : form} )

def BlogTagView(request, tag):
    search_query = request.GET.get('search' , '')
    if search_query:
        object_list = Post.objects.all().filter(Q(text__icontains=search_query))
    else:
        object_list = Post.objects.filter(tag=tag)

    return render(request, 'blog.html', {'object_list' : object_list})
