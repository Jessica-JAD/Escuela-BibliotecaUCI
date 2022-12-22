from django import forms
from apps.adquisiciones.models import Adquisicion

class fr_adquisicion(forms.ModelForm):
    class Meta:
        model = Adquisicion
        fields = '__all__'