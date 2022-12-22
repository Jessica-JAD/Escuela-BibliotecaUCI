# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from apps.app import views
from .views import quienesso, servicios

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('quienessomos/',quienesso.as_view(),name='quienessomos'),
    path('servicios/',servicios.as_view(),name='servicios'),
    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
