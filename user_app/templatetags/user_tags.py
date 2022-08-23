from django import template

register = template.Library()


@register.filter()
def total(value):
    total_values = len(value)
    return total_values



