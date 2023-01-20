from django import forms
from apps.consultatramite.models import ConsultaTramite

class fr_consultatramite(forms.ModelForm):
    class Meta:
        model = ConsultaTramite
        fields = ('nombreusuario', 'descripcion')

class fr_consultatramiteResp(forms.ModelForm):
    class Meta:
        model = ConsultaTramite
        fields = ('respuesta',)