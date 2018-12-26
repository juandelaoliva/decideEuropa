from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import TwoStepsAuth
from authentication.services import check_if_user_exists
from rest_framework.authtoken.models import Token

class UserDecideForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 == password2:
            raise forms.ValidationError(
                _("The passwords doesn't match"),
                code = 'not_matching_passwords'
            )

class RequestAuthEmailForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        try:
            user = User.objects.get(email = email)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("This email doesn't exist"),
                code = 'not_existent_email')
        try:
            token = Token.objects.get(user = user)
            raise forms.ValidationError(_("The user is already logged"),
                code = 'user_already_logged')
        except ObjectDoesNotExist:
            pass

class LoginAuthEmailForm(forms.Form):
    email = forms.EmailField()
    code = forms.CharField(max_length=192)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        code = cleaned_data.get('code')
        try:
            user = User.objects.get(email = email)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("This email doesn't exist"),
                code = 'not_existent_email'
            )
        try:
            two_steps_auth = TwoStepsAuth.objects.get(user = user, code = code)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("Your email login petition isn't registered in the system"),
                code = 'not_existent_two_steps_auth'
            )
        try:
            user = User.objects.get(email = email)
            token = Token.objects.get(user = user)
            raise forms.ValidationError(_("El usuario ya está autenticado en el sistema"),
            code = 'token_already_created',
            params = {},)
        except ObjectDoesNotExist:
            pass
