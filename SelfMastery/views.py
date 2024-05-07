
# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Page, Blog

def home(request):
    categories = Category.objects.all()
    pages = Page.objects.filter(is_published=True)
    posts = Blog.objects.filter(status=1)
    return render(request, 'home.html', {'categories': categories, 'pages': pages, 'posts': posts})

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def about(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'about.html', {'posts': posts})

def blog(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'blog.html', {'pages': pages})

def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=1)
    return render(request, 'post_detail.html', {'post': post})

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug, is_published=True)
    return render(request, 'page_detail.html', {'page': page})
