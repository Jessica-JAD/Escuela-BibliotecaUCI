from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.noticia.forms import fr_Noticia
from apps.noticia.models import Noticia


class CreateNoticia(LoginRequiredMixin,CreateView):
    model = Noticia
    form_class = fr_Noticia
    template_name = 'noticias/cp_crearNoticia.html'
    success_url = reverse_lazy('listarnoticia')

class ListNoticia(LoginRequiredMixin,ListView):
    model = Noticia
    queryset = Noticia.objects.all()
    template_name = 'noticias/cp_listarNoticia.html'

class DeleteNoticia(LoginRequiredMixin,DeleteView):
    model = Noticia
    template_name = 'noticias/cp_eliminarNoticia.html'
    success_url = reverse_lazy('listarnoticia')
