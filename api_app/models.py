from django.db import models

# Create your models here.
class DemoStudent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
