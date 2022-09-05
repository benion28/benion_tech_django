from django.db import models
from datetime import datetime


# Create your models here.
class ChatUser(models.Model):
    username = models.CharField(max_length=15)
    nickname = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.username}({self.nickname})'


class Room(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Message(models.Model):
    value = models.CharField(default='', max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    sender = models.CharField(default='', max_length=15)
    reciever = models.CharField(default='', max_length=15)
    room = models.CharField(default='', max_length=15)

    def __str__(self):
        return f'{self.sender} ({self.room})'

