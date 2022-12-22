from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.bibliografia.forms import fr_InsertarBibliografiaEspecializada
from apps.bibliografia.models import BibliografiaEsp


class CreateBibliografia(LoginRequiredMixin,CreateView):
    model = BibliografiaEsp
    form_class = fr_InsertarBibliografiaEspecializada
    template_name = 'bibliografia/crearbibliografia.html'
    success_url = reverse_lazy('listarbibliografia')

class ListBibliografia(LoginRequiredMixin,ListView):
    model = BibliografiaEsp
    queryset = BibliografiaEsp.objects.all()
    template_name = 'bibliografia/cp_listarBibliografiaEspecializada.html'

class UpdateBibliografia(LoginRequiredMixin,UpdateView):
    model = BibliografiaEsp
    template_name = 'bibliografia/modificarbibliografia.html'
    form_class = fr_InsertarBibliografiaEspecializada
    success_url = reverse_lazy('listarbibliografia')

class DeleteBibliografia(LoginRequiredMixin,DeleteView):
    model = BibliografiaEsp
    template_name = 'bibliografia/eliminarbibliografia.html'
    success_url = reverse_lazy('listarbibliografia')
