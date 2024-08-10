from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User

from aplicaciones.core.models import ListaNegra, TerminosYCondiciones


# Formulario de registro de usuario
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        # Verificar si el nombre de usuario o correo electrónico están en la lista negra
        if ListaNegra.objects.filter(username=username).exists() or ListaNegra.objects.filter(email=email).exists():
            raise forms.ValidationError("No puedes registrar una cuenta con estos datos porque están en la lista negra.")

        return cleaned_data
    

#formulario de login
class CustomLoginForm(AuthenticationForm):
    pass

#formulario para recuperar contraseña
class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No existe un usuario con ese correo electrónico.")
        return email


# Formulario para confirmar contraseña antes de eliminar cuenta
class ConfirmPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

# Formulario para restablecer la contraseña
class CustomSetPasswordForm(SetPasswordForm):
    pass


#formulario para cambiar contraseña una vez esta autenticado el usuario
class CustomPasswordChangeForm(PasswordChangeForm):
    pass

#-------------------------------------------------------------------------------------------------------------
#formulario para aceptar terminos y condiciones
class TerminosYCondicionesForm(forms.ModelForm):
    class Meta:
        model = TerminosYCondiciones
        fields = ['aceptado']

        widgets = {
            'aceptado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Añadir clases CSS
        }
        labels = {
            'aceptado': 'Acepto los términos y condiciones',  # Etiqueta personalizada
        }

    def clean_aceptado(self):
        data = self.cleaned_data.get("aceptado")
       # if not data:
        #    raise forms.ValidationError("Debes aceptar los términos y condiciones para continuar.")        
        return data
#-------------------------------------------------------------------------------------------------------------