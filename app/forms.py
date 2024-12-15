from django import forms
from .models import Punto

class PuntoForm(forms.ModelForm):
    class Meta:
        model = Punto
        fields = ['area', 'estado', 'comentarios', 'certificado']
