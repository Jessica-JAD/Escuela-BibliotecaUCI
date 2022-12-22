from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
from apps.asistenciaespecializada.forms import fr_AsistenciaEspecializada
from apps.asistenciaespecializada.models import AsistenciaEspecializada


class CreateAsistenciaEspecializada(LoginRequiredMixin,CreateView):
    model = AsistenciaEspecializada
    form_class = fr_AsistenciaEspecializada
    template_name = 'asistenciaespecializada/crearaasistenciaespecializada.html'
    success_url = reverse_lazy('listarasistenciaespecializada')

class ListAsistenciaEspecializada(LoginRequiredMixin,ListView):
    model = AsistenciaEspecializada
    queryset = AsistenciaEspecializada.objects.all()
    template_name = 'asistenciaespecializada/listarasistenciaespecializada.html'


class DeleteAsistenciaEspecializada(LoginRequiredMixin,DeleteView):
    model = AsistenciaEspecializada
    template_name = 'asistenciaespecializada/eliminarasistenciaespecializada.html'
    success_url = reverse_lazy('listarasistenciaespecializada')

