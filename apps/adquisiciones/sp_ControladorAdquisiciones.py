from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from apps.adquisiciones.forms import fr_adquisicion
from apps.adquisiciones.models import Adquisicion


class CreateAdquisicion(LoginRequiredMixin,CreateView):
    model = Adquisicion
    form_class = fr_adquisicion
    template_name = 'adquisiciones/crearadquisicion.html'
    success_url = reverse_lazy('listaradquisicion')

class ListAdquisicion(LoginRequiredMixin,ListView):
    model = Adquisicion
    queryset = Adquisicion.objects.all()
    template_name = 'adquisiciones/listaradquisicion.html'


class DeleteAdquisicion(LoginRequiredMixin,DeleteView):
    model = Adquisicion
    template_name = 'adquisiciones/eliminaradquisicion.html'
    success_url = reverse_lazy('listaradquisicion')


