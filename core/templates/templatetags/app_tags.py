from datetime import timedelta
from django import template

register = template.Library()


@register.filter
def convert(seconds):
    # return time.strftime("%H:%M:%S", time.gmtime(seconds))
    return "{:0>8}".format(str(timedelta(seconds=seconds)))


register.filter = ('convert', convert)