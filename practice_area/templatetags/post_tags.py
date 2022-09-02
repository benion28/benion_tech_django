from django import template
from django.contrib.auth.models import User
from user_app.models import UserDetail

register = template.Library()


@register.filter()
def total(value):
    total_values = len(value)
    return total_values


@register.filter()
def get_name(username):
    user = User.objects.get(username=username)
    return f"{user.first_name} {user.last_name}"


@register.filter()
def truncate_text(value):
    text = value[0: 500]
    text += "..."
    return text


@register.filter()
def reduce_text(value):
    text = value[0: 100]
    text += "..."
    return text


@register.filter()
def get_profile(username):
    profile = "https://firebasestorage.googleapis.com/v0/b/benion-database.appspot.com/o/Benion%20Tech%2Fuser.png?alt=media&token=4d9c743f-3105-42f9-9d93-c800ec0c92c4"
    user_details = UserDetail.objects.get(username=username)
    if user_details.profile != "null":
        profile = user_details.profile
    return profile


@register.filter()
def first_character(value):
    return value[0]


@register.filter()
def rest_character(value):
    return value[1:]
