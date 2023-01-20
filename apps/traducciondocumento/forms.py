from django import forms
from apps.traducciondocumento.models import TraduccionDocumento

class fr_traduccionDocumento(forms.ModelForm):
    class Meta:
        model = TraduccionDocumento
        fields = '__all__'
