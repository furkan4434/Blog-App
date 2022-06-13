from tkinter import CASCADE
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='posts', null=True, blank=True)
    description = RichTextField()
    summary = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
