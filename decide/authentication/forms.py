from django import forms
from django.utils.translation import gettext_lazy as _

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
