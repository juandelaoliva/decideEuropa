from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView
from authentication.forms import UserDecideForm, RequestAuthEmailForm, LoginAuthEmailForm, ActivateAccountForm
from authentication.models import UserDecide, TwoStepsAuth, UserStatus
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.contrib.sessions.models import Session
from authentication.services import send_mail_2_steps_auth, login_email_auth, activate_account_recently_registered, register_user
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

    @transaction.atomic
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
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
        two_steps_auth = register_user(username, password, email, first_name, last_name)
        send_mail('Bienvenido a Decide', 
            ''.join(('Use el siguiente código para verificar tu identidad y confirmar tu registro en la aplicación\r\n\r\n', 
            str(two_steps_auth.code))), 'decide@decide.com', [two_steps_auth.user.email], fail_silently = False)
        return HttpResponseRedirect('/authentication/activate-account/')

class ActivateAccountView(FormView):
    template_name = 'activate_account.html'
    form_class = ActivateAccountForm

    @transaction.atomic
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        code = form.cleaned_data['code']
        activate_account_recently_registered(username, password, code)
        return HttpResponseRedirect('/authentication/')


class RequestAuthEmailCodeView(FormView):
    template_name = 'request_auth_email.html'
    form_class = RequestAuthEmailForm
    success_url = '/authentication/login-auth-email/'

    def get(self, request):
        response = check_user_status_view(request, unauthenticated_required = True, unauthenticated_allowed = True)
        if response == None:
            response = super().get(self, request)
        return response

    @transaction.atomic
    def post(self, request):
        response = check_user_status_view(request, unauthenticated_required = True, unauthenticated_allowed = True)
        if response == None:
            response = super().post(self, request)
            form = self.form_class(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                session_token = request.session.get('token')
                two_steps_auth = send_mail_2_steps_auth(username, password, session_token)
                send_mail('Autenticación en Decide mediante email', ''.join(('Use el siguiente código para autenticarse en el' +  
                    'sistema\r\n\r\n', str(two_steps_auth.code))), 'decide@decide.com', [two_steps_auth.user.email], fail_silently = False)
        return response

class LoginEmailCodeView(FormView):
    template_name = 'login_auth_email.html'
    form_class = LoginAuthEmailForm
    success_url = '/booth/votings/'

    def get(self, request):
        response = check_user_status_view(request, unauthenticated_required = True, unauthenticated_allowed = True)
        if response == None:
            response = super().get(self, request)
        return response
    
    @transaction.atomic
    def post(self, request):
        response = check_user_status_view(request, unauthenticated_required = True, unauthenticated_allowed = True)
        if response == None:
            response = super().post(self, request)
            form = self.form_class(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                code = form.cleaned_data['code']
                session_token = request.session.get('token')
                token = login_email_auth(username, password, code, session_token)
                request.session['token'] = token.key
        return response

class LogoutSessionView(TemplateView):
    template_name = 'logout.html'

    def get(self, request):
        check_user_status_view(request, list_status_allowed = ['ACTIVE'], unauthenticated_allowed = True)
        session_token = request.session.get('token')
        print(request.session.get_expire_at_browser_close())
        try:
            Token.objects.get(key = session_token).delete()
        except ObjectDoesNotExist:
            pass
        request.session.flush()
        response = super().get(request)
        return response
        
class LogoutView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        try:
            tk = Token.objects.get(key=key)
            tk.delete()
        except ObjectDoesNotExist:
            pass

        return Response({})

def check_user_status_view(request, list_status_allowed = [], unauthenticated_allowed = False, unauthenticated_required = False):
    try:
        session_token = request.session.get('token')
        if session_token == None:
            if not unauthenticated_allowed:
                return render(request, 'unallowed.html')
        else:
            token_object = Token.objects.get(key = session_token)
            user = token_object.user
            user_status = UserStatus.objects.get(user = user)
            if user_status.status not in list_status_allowed or unauthenticated_required:
                return render(request, 'unallowed.html')
    except ObjectDoesNotExist:
        del request.session['token']
        if not unauthenticated_allowed:
            return render(request, 'unallowed.html')
        

