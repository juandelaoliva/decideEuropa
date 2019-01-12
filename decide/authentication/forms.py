from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import TwoStepsAuth, UserStatus
from authentication.services import check_if_user_exists, search_user_by_username_and_password
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

class UserDecideForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not password1 == password2:
            raise forms.ValidationError(
                _("The passwords doesn't match"),
                code = 'not_matching_passwords'
            )
        try:
            user = User.objects.get(username = username)
            raise forms.ValidationError(
                _("There is already a user account with that username"),
                code = 'username_must_unique')
        except ObjectDoesNotExist:
            pass

class RequestAuthEmailForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        hashed_password = make_password(password)
        try:
            user = search_user_by_username_and_password(username, password)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("This account doesn't exist"),
                code = 'not_existent_account')

class LoginAuthEmailForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)
    code = forms.CharField(max_length=192)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        code = cleaned_data.get('code')

        try:
            user = search_user_by_username_and_password(username, password)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("This account doesn't exist"),
                code = 'not_existent_account'
            )
        try:
            two_steps_auth = TwoStepsAuth.objects.get(user = user, code = code)
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("Your login petition isn't registered in the system"),
                code = 'not_existent_two_steps_auth'
            )

class ActivateAccountForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput)
    code = forms.CharField(max_length=192)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        code = cleaned_data.get('code')

        try:
            user = search_user_by_username_and_password(username, password)
            user_status = UserStatus.objects.get(user = user)
            if not user_status.status == 'RECENTLY_REGISTERED':
                raise forms.ValidationError(_("The user has already activated his/her account"),
                    code = 'account_already_activated'
                )
        except ObjectDoesNotExist:
            raise forms.ValidationError(_("This account doesn't exist"),
                code = 'not_existent_account'
            )
