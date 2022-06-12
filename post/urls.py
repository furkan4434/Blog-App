from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/sport/', views.sport, name='sport'),
    path('categories/healtyEating/', views.healtyEating, name='healtyEating'),
    path('categories/fashion/', views.fashion, name='fashion'),
    path('categories/recipes/', views.recipes, name='recipes'),
    path('blog_details/<str:pk>/', views.blog_details, name='blog_details')
]