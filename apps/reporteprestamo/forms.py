from django import forms
from apps.reporteprestamo.models import ReportePrestamo

class fr_InsertarReportePrestamo(forms.ModelForm):
    class Meta:
        model = ReportePrestamo
        fields = '__all__'