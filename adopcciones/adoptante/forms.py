from django import forms
from .models import Persona, Solicitud

class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = [
			'name',
			'last_name',
			'age',
			'telephone',
			'email',
			'home',
		]
		labels = {
			'name':'Nombre',
			'last_name':'Apellido',
			'age': 'Edad',
			'telephone':'Telefono',
			'email':'Correo electronico',
			'home':'Domicilio',
		}
		widgets = {
			'name':forms.TextInput(attrs={'class':'form-control'}),
			'last_name:':forms.TextInput(attrs={'class':'form-control'}),
			'age':forms.TextInput(attrs={'class':'form-control'}),
			'telephone':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'home':forms.Textarea(attrs={'class':'form-control'}),
		}


class SolicitudForm(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = [
			'razones',	
		]
		labels = {
			'razones': 'Razones para adoptar',		
		}
		widgets = {
			'razones':forms.Textarea(attrs={'class':'form-control'}),
		}
