from django.db import models


# Create your models here.
class DemoItem(models.Model):
    firstname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    lastname = models.CharField(max_length=20)

