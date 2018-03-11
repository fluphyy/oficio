from django import forms
from django.forms import DateInput, TextInput, NumberInput, Textarea
from oficio.models import Oficio


class FormOficio(forms.ModelForm):
    error = 'Erro'
    class Meta:
        model = Oficio
        fields = ['numero', 'data', 'para', 'cargo_para', 'assunto', 'texto']
        widgets = {
            'data': DateInput(attrs={'class':'data form-control'}),
            'numero': NumberInput(attrs={'class':'form-control'}),
            'para': TextInput(attrs={'class':'form-control'}),
            'cargo_para': TextInput(attrs={'class':'form-control'}),
            'assunto': TextInput(attrs={'class':'form-control'}),
            'texto': Textarea(attrs={'class':'form-control'}),

        }