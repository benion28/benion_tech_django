from django.contrib import admin
from .models import ChatUser, Message, Room


# Register your models here.
admin.site.register(ChatUser)
admin.site.register(Message)
admin.site.register(Room)
