"""
Docstring pendiente para este documento
"""


from django.conf.urls import patterns, url, include
from api.views import ClienteViewSet
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'apiv01cliente', ClienteViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )
