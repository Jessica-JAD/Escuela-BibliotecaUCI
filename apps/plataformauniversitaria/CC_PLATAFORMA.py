from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.plataformauniversitaria.forms import FORMINSERTAR
from apps.plataformauniversitaria.models import PLATAFORMAU


class CreatePlatformaUniversitaria(LoginRequiredMixin,CreateView):
    model = PLATAFORMAU
    form_class = FORMINSERTAR
    template_name = 'plataformauniversitaria/crearplataformauniversitaria.html'
    success_url = reverse_lazy('listarplataformauniversitaria')

class ListPlatformaUniversitaria(LoginRequiredMixin,ListView):
    model = PLATAFORMAU
    queryset = PLATAFORMAU.objects.all()
    template_name = 'plataformauniversitaria/CI_LISTA.html'

class UpdatePlatformaUniversitaria(LoginRequiredMixin,UpdateView):
    model = PLATAFORMAU
    template_name = 'plataformauniversitaria/modificarplataformauniversitaria.html'
    form_class = FORMINSERTAR
    success_url = reverse_lazy('listarplataformauniversitaria')

class DeletePlatformaUniversitaria(LoginRequiredMixin,DeleteView):
    model = PLATAFORMAU
    template_name = 'plataformauniversitaria/eliminarplataformauniversitaria.html'
    success_url = reverse_lazy('listarplataformauniversitaria')
