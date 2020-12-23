from django.shortcuts import render, get_object_or_404
from .models import Post, Gallery
from django.contrib.auth import authenticate
from django.views.generic import DetailView

def index(request):
    posts = Post.objects.all()
    return render(request, 'bord/index.html', {'posts': posts})


def post_page(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'bord/page.html', {'post': post})
