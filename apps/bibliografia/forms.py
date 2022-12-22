from django import forms
from apps.bibliografia.models import BibliografiaEsp

class fr_InsertarBibliografiaEspecializada(forms.ModelForm):
    class Meta:
        model = BibliografiaEsp
        fields = '__all__'