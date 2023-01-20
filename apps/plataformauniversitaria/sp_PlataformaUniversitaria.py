from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.plataformauniversitaria.forms import fr_InsertarPlataforma
from apps.plataformauniversitaria.models import plataformaU


class CreatePlatformaUniversitaria(LoginRequiredMixin,CreateView):
    model = plataformaU
    form_class = fr_InsertarPlataforma
    template_name = 'plataformauniversitaria/cp_crearPlataforma.html'
    success_url = reverse_lazy('listarplataformauniversitaria')

class ListPlatformaUniversitaria(LoginRequiredMixin,ListView):
    model = plataformaU
    queryset = plataformaU.objects.all()
    template_name = 'plataformauniversitaria/cp_listarPlataforma.html'

class UpdatePlatformaUniversitaria(LoginRequiredMixin,UpdateView):
    model = plataformaU
    template_name = 'plataformauniversitaria/cp_modificarPlataforma.html'
    form_class = fr_InsertarPlataforma
    success_url = reverse_lazy('listarplataformauniversitaria')

class DeletePlatformaUniversitaria(LoginRequiredMixin,DeleteView):
    model = plataformaU
    template_name = 'plataformauniversitaria/cp_eliminarPlataforma.html'
    success_url = reverse_lazy('listarplataformauniversitaria')
