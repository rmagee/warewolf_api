# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from warewolf_api.urls import urlpatterns as warewolf_api_urls

app_name = 'warewolf_api'

urlpatterns = [
    url(r'^', include(warewolf_api_urls)),
]
