from django.db import models
from datetime import datetime


# Create your models here.
class DemoItem(models.Model):
    firstname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    lastname = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    creator = models.CharField(max_length=20)
    image = models.CharField(max_length=150)
    date = models.DateTimeField(default=datetime.now, blank=True)
    content = models.TextField(max_length=3000)
    category = models.CharField(max_length=15)
    tag = models.CharField(max_length=15)
    key = models.CharField(max_length=30)

