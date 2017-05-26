from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
#
#
# class SignUpForm(forms.Form):
#     username = forms.CharField(max_length=50, label=False,
#                                widget=forms.TextInput(attrs={'placeholder': _('Username')}))
#     email = forms.CharField(label=False, widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
#     password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))
#     password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': _('Repeat password')}))
#
#     def clean(self):
#
#         user_exists = User.objects.filter(username=self.cleaned_data.get("username"))
#
#         if len(user_exists) != 0:
#             raise ValidationError(_('This user already exists'))
#
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError(_("Passwords doesn't match"))

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de usuario',
            'email': 'Dirección de correo',
            'password': 'Contraseña',
        }

        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')




