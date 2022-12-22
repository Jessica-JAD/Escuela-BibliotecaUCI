from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.noticia.forms import fr_AdministrarNoticia
from apps.noticia.models import Noticia


class CreateNoticia(LoginRequiredMixin,CreateView):
    model = Noticia
    form_class = fr_AdministrarNoticia
    template_name = 'noticias/crearnoticia.html'
    success_url = reverse_lazy('listarnoticia')

class ListNoticia(LoginRequiredMixin,ListView):
    model = Noticia
    queryset = Noticia.objects.all()
    template_name = 'noticias/cp_AdministrarNoticia.html'

class DeleteNoticia(LoginRequiredMixin,DeleteView):
    model = Noticia
    template_name = 'noticias/eliminarnoticia.html'
    success_url = reverse_lazy('listarnoticia')
