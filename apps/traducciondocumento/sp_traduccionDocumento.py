from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.traducciondocumento.forms import fr_traduccionDocumento
from apps.traducciondocumento.models import TraduccionDocumento


class CreateTraduccionDocumento(LoginRequiredMixin,CreateView):
    model = TraduccionDocumento
    form_class = fr_traduccionDocumento
    template_name = 'traducciondocumento/creartraducciondocumento.html'
    success_url = reverse_lazy('listartraducciondocumento')

class ListTraduccionDocumento(LoginRequiredMixin,ListView):
    model = TraduccionDocumento
    queryset = TraduccionDocumento.objects.all()
    template_name = 'traducciondocumento/listartraducciondocumento.html'

class DeleteTraduccionDocumento(LoginRequiredMixin,DeleteView):
    model = TraduccionDocumento
    template_name = 'traducciondocumento/eliminartraducciondocumento.html'
    success_url = reverse_lazy('listartraducciondocumento')
