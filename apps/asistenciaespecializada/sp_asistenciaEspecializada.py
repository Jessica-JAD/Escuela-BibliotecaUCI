from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from apps.asistenciaespecializada.forms import fr_AsistenciaEspecializada, fr_AsistenciaEspecilizadaResp
from apps.asistenciaespecializada.models import AsistenciaEspecializada


class CreateAsistenciaEspecializada(LoginRequiredMixin,CreateView):
    model = AsistenciaEspecializada
    form_class = fr_AsistenciaEspecializada
    template_name = 'asistenciaespecializada/cp_crearAsistenciaEspecializada.html'
    success_url = reverse_lazy('listarasistenciaespecializada')

class ListAsistenciaEspecializada(ListView):
    model = AsistenciaEspecializada
    queryset = AsistenciaEspecializada.objects.all()
    template_name = 'asistenciaespecializada/cp_listarAsistenciaEspecializada.html'


class DeleteAsistenciaEspecializada(LoginRequiredMixin,DeleteView):
    model = AsistenciaEspecializada
    template_name = 'asistenciaespecializada/cp_eliminarAsistenciaEspecializada.html'
    success_url = reverse_lazy('listarasistenciaespecializada')

class UpdateAsistenciaEspecializada(LoginRequiredMixin,UpdateView):
    model = AsistenciaEspecializada
    template_name = 'asistenciaespecializada/cp_modificarAsisteciaEspecializada.html'
    form_class = fr_AsistenciaEspecilizadaResp
    success_url = reverse_lazy('listarasistenciaespecializada')

