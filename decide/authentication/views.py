from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from authentication.forms import UserDecideForm
from django.db import transaction
from django.http import HttpResponse
from django import forms
from django.views import View
from django.core.mail import send_mail
import _random as random
import _string as string

from .serializers import UserSerializer

class GetUserView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        tk = get_object_or_404(Token, key=key)

        return Response(UserSerializer(tk.user, many=False).data)

class RegisterUserView(FormView):
    template_name = 'user_register.html'
    form_class = UserDecideForm
    success = 'localhost:8080'

    @transaction.atomic
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = make_password(form.cleaned_data['password1'])
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        if not username:
            raise forms.ValidationError("The username is blank",
                                        code='username_blank'
            )
        if not password:
            raise forms.ValidationError("The password is blank",
                                        code='password_blank'
                                        )
        if not first_name:
            raise forms.ValidationError("The first name is blank",
                                        code='first_name_blank'
                                        )
        if not last_name:
            raise forms.ValidationError("The last name is blank",
                                        code='last_name_blank'
                                        )
        if not email:
            raise forms.ValidationError("The email is blank",
                                        code='email_blank'
                                        )
        user = User(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        user.save()
        return Response({})

class LogoutView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        try:
            tk = Token.objects.get(key=key)
            tk.delete()
        except ObjectDoesNotExist:
            pass

        return Response({})
