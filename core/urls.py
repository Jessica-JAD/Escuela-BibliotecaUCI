# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.app.urls")),
    path("", include("apps.bibliografia.urls")),
    path("", include("apps.noticia.urls")),
    path("", include("apps.adquisiciones.urls")),
    path("", include("apps.curso.urls")),
    path("", include("apps.plataformauniversitaria.urls")),
    path("", include("apps.asistenciaespecializada.urls")),
    path("", include("apps.reporteprestamo.urls")),
    path("", include("apps.traducciondocumento.urls")),
    path("", include("apps.consultatramite.urls"))

]
