# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .forms import LoginForm, fr_crearUser
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Credenciales incorrectas'
        else:
            msg = 'Error al validar los datos'

    return render(request, "accounts/cp_autenticar.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = fr_crearUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuario creado con exito'
            success = True

            return redirect("/login/")

        else:
            msg = 'El formulario no es válido'
    else:
        form = fr_crearUser()

    return render(request, "accounts/cp_registrar.html", {"form": form, "msg": msg, "success": success})

class ListUsuario(LoginRequiredMixin,ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'usuario/cp_listarUsuario.html'

class DeleteUsuario(LoginRequiredMixin,DeleteView):
    model = User
    template_name = 'usuario/cp_eliminarUsuario.html'
    success_url = reverse_lazy('listarusuario')
