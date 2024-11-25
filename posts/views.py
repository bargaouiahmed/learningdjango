from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
def posts(request):
    posts = Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts} )
def post_page(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html',{'post':post})
@login_required(login_url="/users/login/")
def posts_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('posts:posts_list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/posts_new.html', {'form': form})
