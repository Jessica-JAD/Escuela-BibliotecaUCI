from django import forms
from apps.asistenciaespecializada.models import AsistenciaEspecializada

class fr_AsistenciaEspecializada(forms.ModelForm):
    class Meta:
        model = AsistenciaEspecializada
        fields = ('tipo', 'descripcion')

class fr_AsistenciaEspecilizadaResp(forms.ModelForm):
    class Meta:
        model = AsistenciaEspecializada
        fields = ('respuesta',)