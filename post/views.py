from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'navbar':'Home', 'posts':posts}
    return render(request, 'post/main.html',context)

def sport(request):
    posts = Post.objects.filter(category__categoryName = "Sport")
    
    context = {'navbar':'Sport','posts':posts}
    return render(request, 'post/sport.html', context)

def healtyEating(request):
    posts = Post.objects.filter(category__categoryName = "Healthy eating")
    
    context = {'navbar':'HealthyEating','posts':posts}
    return render(request, 'post/sport.html', context)

def fashion(request):
    posts = Post.objects.filter(category__categoryName = "Fashion")
    
    context = {'navbar':'Fashion','posts':posts}
    return render(request, 'post/sport.html', context)

def recipes(request):
    posts = Post.objects.filter(category__categoryName = "Recipes")
    
    context = {'navbar':'Recipes','posts':posts}
    return render(request, 'post/sport.html', context)

def blog_details(request, pk):

    blog_detail = Post.objects.get(id=pk)

    context = {'navbar':"blog_details", 'posts':blog_detail}

    return render(request, 'post/blog_details.html', context)


