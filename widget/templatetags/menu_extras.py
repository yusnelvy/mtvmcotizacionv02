from django import template
from django.core.urlresolvers import reverse
from menu.models import Menu, Relacion

register = template.Library()


@register.simple_tag
def url_Menu(namespace, name):
    """docstring"""
    url = '%s:%s' % (namespace, name)
    urlfinal = reverse(url)
    return (urlfinal)

