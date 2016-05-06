"""
docstring

Pendiente de documentación
"""

from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
                       url(r'^login$',
                           login,
                           {'template_name': 'login.html', },
                           name="login"),
                       url(r'^logout$',
                           logout,
                           {'template_name': 'index.html', },
                           name="logout"),)
