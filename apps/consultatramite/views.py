from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.consultatramite.forms import fr_consultatramite,fr_consultatramiteResp
from apps.consultatramite.models import ConsultaTramite


class CreateConsultaTramite(LoginRequiredMixin,CreateView):
    model = ConsultaTramite
    form_class = fr_consultatramite
    template_name = 'consultatramite/cp_crearconsultatramite.html'
    success_url = reverse_lazy('listarconsultatramite')

class ListConsultaTramite(LoginRequiredMixin,ListView):
    model = ConsultaTramite
    queryset = ConsultaTramite.objects.all()
    template_name = 'consultatramite/cp_listarconsultatramite.html'

class UpdateConsultaTramite(LoginRequiredMixin,UpdateView):
    model = ConsultaTramite
    template_name = 'consultatramite/cp_modificarconsultatramite.html'
    form_class = fr_consultatramiteResp
    success_url = reverse_lazy('listarconsultatramite')

class DeleteConsultaTramite(LoginRequiredMixin,DeleteView):
    model = ConsultaTramite
    template_name = 'consultatramite/cp_eliminarconsultatramite.html'
    success_url = reverse_lazy('listarconsultatramite')
