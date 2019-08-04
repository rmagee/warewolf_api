# -*- coding: utf-8 -*-
from django.conf.urls import url
from warewolf_api import views

from . import views

urlpatterns = [
    url(r'^item-detail/(?P<barcode>[0-9a-zA-Z\W]{1,150})/$',
        views.GetItemDetail.as_view(),
        name='item-detail')
    ]
