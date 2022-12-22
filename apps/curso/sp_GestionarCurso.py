from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.curso.forms import fr_InsertarCurso
from apps.curso.models import Curso


class CreateCurso(LoginRequiredMixin,CreateView):
    model = Curso
    form_class = fr_InsertarCurso
    template_name = 'curso/crearcurso.html'
    success_url = reverse_lazy('listarcurso')

class ListCurso(LoginRequiredMixin,ListView):
    model = Curso
    queryset = Curso.objects.all()
    template_name = 'curso/cp_listarCurso.html'

class UpdateCurso(LoginRequiredMixin,UpdateView):
    model = Curso
    template_name = 'curso/modificarcurso.html'
    form_class = fr_InsertarCurso
    success_url = reverse_lazy('listarcurso')

class DeleteCurso(LoginRequiredMixin,DeleteView):
    model = Curso
    template_name = 'curso/eliminarcurso.html'
    success_url = reverse_lazy('listarcurso')
