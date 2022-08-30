from django import template
from benion_tech_django.settings import env
from benion_tech_django.helpers.cbt_users import get_cbt_users
from benion_tech_django.helpers.scores import get_scores
from benion_tech_django.helpers.exams import get_exams
from benion_tech_django.helpers.messages import get_messages
from user_app.models import CbtUser, CbtExam, ExamScore, ContactMessage

register = template.Library()
production = env('PRODUCTION')


@register.filter()
def total(value):
    total_values = len(value)
    return total_values


@register.filter()
def cbt_users_sn(params):
    data = CbtUser.objects.all()
    items = []
    for item in data:
        items.append(item)
    all_cbt_users = items
    if production:
        all_cbt_users = get_cbt_users()
    index = all_cbt_users.index(params) + 1
    return index


@register.filter()
def scores_sn(params):
    data = ExamScore.objects.all()
    items = []
    for item in data:
        items.append(item)
    all_scores = items
    if production:
        all_scores = get_scores()
    index = all_scores.index(params) + 1
    return index


@register.filter()
def exams_sn(params):
    data = CbtExam.objects.all()
    items = []
    for item in data:
        items.append(item)
    all_exams = items
    if production:
        all_exams = get_exams()
    index = all_exams.index(params) + 1
    return index


@register.filter()
def messages_sn(params):
    data = ContactMessage.objects.all()
    items = []
    for item in data:
        items.append(item)
    all_messages = items
    if production:
        all_messages = get_messages()
    index = all_messages.index(params) + 1
    return index
