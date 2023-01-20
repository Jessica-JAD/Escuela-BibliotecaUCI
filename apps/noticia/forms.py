from django import forms
from apps.noticia.models import Noticia

class fr_Noticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'