from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=500)
    blog_entry = models.CharField(max_length=10000)