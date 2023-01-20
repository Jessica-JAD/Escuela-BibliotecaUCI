from django import forms
from apps.plataformauniversitaria.models import plataformaU

class fr_InsertarPlataforma(forms.ModelForm):
    class Meta:
        model = plataformaU
        fields = '__all__'