from django import template

register = template.Library()


@register.simple_tag
def so_many_images(value, count):
    return ' '.join([value] * count)