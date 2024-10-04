from django import forms
from .models import Events


class EventoForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['titulo', 'descripcion', 'fecha', 'capacidad']
