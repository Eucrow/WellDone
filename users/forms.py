from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50, label=False,
                               widget=forms.TextInput(attrs={'placeholder': _('User name')}))
    first_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': _('Name')}))
    last_name = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': _('Surname')}))
    email = forms.CharField(label=False, widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
    password1 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))
    password2 = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder': _('Repeat password')}))

    def clean(self):

        user_exists = User.objects.filter(username=self.cleaned_data.get("username"))

        if len(user_exists) != 0:
            raise ValidationError('This user already exists')

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords doesn't match"))



