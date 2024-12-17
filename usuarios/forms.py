from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefono', 'direccion', 'password1', 'password2']
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'telefono': 'Número de Teléfono',
            'direccion': 'Dirección',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

class EditarPerfilForm(UserChangeForm):
    password = None  
    class Meta:
        model = Usuario
        fields = ['email', 'telefono', 'direccion']
        labels = {
            'email': 'Correo Electrónico',
            'telefono': 'Número de Teléfono',
            'direccion': 'Dirección',
        }
