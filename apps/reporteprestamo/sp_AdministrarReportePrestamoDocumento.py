from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.reporteprestamo.forms import fr_InsertarReportePrestamo
from apps.reporteprestamo.models import ReportePrestamo


class CreateReportePrestamo(LoginRequiredMixin,CreateView):
    model = ReportePrestamo
    form_class = fr_InsertarReportePrestamo
    template_name = 'reporteprestamo/crearreporteprestamo.html'
    success_url = reverse_lazy('listarreporteprestamo')

class ListReportePrestamo(LoginRequiredMixin,ListView):
    model = ReportePrestamo
    queryset = ReportePrestamo.objects.all()
    template_name = 'reporteprestamo/cp_listarReportePrestamosDocumento.html'

class DeleteReportePrestamo(LoginRequiredMixin,DeleteView):
    model = ReportePrestamo
    template_name = 'reporteprestamo/eliminarreporteprestamo.html'
    success_url = reverse_lazy('listarreporteprestamo')
