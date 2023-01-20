# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .sp_controladorUsuario import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.authentication.sp_controladorUsuario import ListUsuario, DeleteUsuario

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("lusuario/", ListUsuario.as_view() , name='listarusuario'),
    path("eusuario/<int:pk>/", DeleteUsuario.as_view(),name='eliminarusuario')

]
