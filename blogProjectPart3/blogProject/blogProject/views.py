from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request, categorySlug = None):
    data = Post.objects.all()
    if categorySlug is not None:
        category = Category.objects.get(slug=categorySlug)
        data = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'home.html', {'data':data, 'category':categories})