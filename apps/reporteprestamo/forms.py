from django import forms
from apps.reporteprestamo.models import ReportePrestamoDocumento

class fr_InsertarReportePrestamoDocumento(forms.ModelForm):
    class Meta:
        model = ReportePrestamoDocumento
        fields = '__all__'