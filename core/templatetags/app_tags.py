from django import template

register = template.Library()


@register.filter
def convert(seconds):
    return str(seconds).split('-')[0]


register.filter = ('convert', convert)