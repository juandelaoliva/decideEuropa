from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from authentication.forms import UserDecideForm, RequestAuthEmailForm, LoginAuthEmailForm
from authentication.models import UserDecide, TwoStepsAuth
from django.db import transaction
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from authentication.services import send_mail_2_steps_auth, login_email_auth
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
        user = User(
            username = username,
            password = password,
            email = email,
            first_name = first_name,
            last_name = last_name
        )
        user.save()
        return HttpResponse()

class RequestAuthEmailCodeView(FormView):
    template_name = 'request_auth_email.html'
    form_class = RequestAuthEmailForm
    success = 'localhost:8080'

    @transaction.atomic
    def form_valid(self, form):
        email = form.cleaned_data['email']
        two_steps_auth = send_mail_2_steps_auth(email)
        send_mail('Autenticación en Decide mediante email', ''.join(('Use el siguiente código para autenticarse en el sistema\r\n\r\n', 
str(two_steps_auth.code))), 'decide@decide.com', [two_steps_auth.user.email], fail_silently = False)
        return HttpResponse()

class LoginEmailCodeView(FormView):
    template_name = 'login_auth_email.html'
    form_class = LoginAuthEmailForm
    success = 'localhost:8080'

    @transaction.atomic
    def form_valid(self, form):
        email = form.cleaned_data['email']
        code = form.cleaned_data['code']
        login_email_auth(email)
        return HttpResponse()

class LogoutView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        try:
            tk = Token.objects.get(key=key)
            tk.delete()
        except ObjectDoesNotExist:
            pass

        return Response({})
