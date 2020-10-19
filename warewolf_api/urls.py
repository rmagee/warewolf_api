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
        name='item-detail'),
    url(
        #https://regex101.com/r/NQXjc1/1
        r'^decommission-parent/(?P<child_urn>(urn:epc:id:sscc:|urn:epc:id:sgtin:)([0-9]*).([0-9]*)?.([0-9\S]*))',
        views.DeleteParentByChild.as_view(),
        name='decommission-parent'
        )
]
urlpatterns += router.urls
