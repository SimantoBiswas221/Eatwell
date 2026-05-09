from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.CharField(max_length=200,unique=True)
    created_on=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
