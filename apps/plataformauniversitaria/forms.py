from django import forms
from apps.plataformauniversitaria.models import PLATAFORMAU

class FORMINSERTAR(forms.ModelForm):
    class Meta:
        model = PLATAFORMAU
        fields = '__all__'