from django import forms
from .models import Infante

class InfanteForm(forms.ModelForm):
    class Meta:
        model = Infante
        fields = [
        	'name',
        	'sex',
        	'age',
        	'date',
        	'persona',
        	'educacion',
    	]
        labels = {
        'name':"nombre",
        'sex':"Sexo",
        'age':"Edad aproximada",
        'date':"Fecha de ingreso al instituto",
        'persona':"Adoptante",
        'educacion':"Grados de educacion",    	
    	}
        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'sex':forms.TextInput(attrs={'class':'form-control'}),
        'age':forms.TextInput(attrs={'class':'form-control'}),
        'date':forms.TextInput(attrs={'class':'form-control'}),
        'persona':forms.Select(attrs={'class':'form-control'}),
        'educacion':forms.CheckboxSelectMultiple(),
    	}