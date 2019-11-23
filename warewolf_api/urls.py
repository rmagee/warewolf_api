# -*- coding: utf-8 -*-
from django.conf.urls import url
from warewolf_api import views

from . import views
from warewolf_api.routers import router

urlpatterns = [
    url(r'^item-detail/(?P<barcode>[0-9a-zA-Z\W]{1,150})/$',
        views.GetItemDetail.as_view(),
        name='item-detail'),
    url(r'^item-detail/?$',
        views.GetItemDetail.as_view(),
        name='item-detail')
    ]

urlpatterns += router.urls

