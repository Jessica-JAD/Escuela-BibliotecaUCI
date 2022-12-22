from django import forms
from apps.curso.models import Curso

class fr_InsertarCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'