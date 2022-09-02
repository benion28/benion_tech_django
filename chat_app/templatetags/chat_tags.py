from django import template
from chat_app.models import Message
from user_app.models import UserDetail

register = template.Library()


@register.filter()
def total_room_messages(value):
    messages = Message.objects.filter(room=value)
    room_messages = len(messages)
    return room_messages


@register.filter()
def total(value):
    total_values = len(value)
    return total_values


@register.filter()
def total_user_messages(value):
    messages = Message.objects.filter(reciever=value)
    user_messages = len(messages)
    return user_messages


@register.filter()
def get_chat_profile(username):
    profile = "https://bootdey.com/img/Content/avatar/avatar5.png"
    user_details = UserDetail.objects.get(username=username)
    if user_details.profile != "null":
        profile = user_details.profile
    return profile
