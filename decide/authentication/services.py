from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError
from authentication.models import TwoStepsAuth
from django.core.exceptions import ObjectDoesNotExist
from Crypto import Random
from rest_framework.authtoken.models import Token
from authentication.exceptions import IllegalArgumentException

def send_mail_2_steps_auth(email):
    u = check_if_user_exists_email(email)
    try:
        token = Token.objects.get(user = u)
        raise IllegalArgumentException(_("The user is already logged"),)
    except ObjectDoesNotExist:
        pass
    code = str(int.from_bytes(Random.new().read(24), 'big'))
    try:	
        old_two_steps_auth = TwoStepsAuth.objects.get(user = u)
        old_two_steps_auth.delete()
        two_steps_auth = TwoStepsAuth.objects.create(code = code, user = u)
    except ObjectDoesNotExist:
        two_steps_auth = TwoStepsAuth.objects.create(code = code, user = u)
    return two_steps_auth

def login_email_auth(email):
    u = check_if_user_exists_email(email)
    try:
        token = Token.objects.get(user = u)
        raise IllegalArgumentException(_("El usuario ya está autenticado en el sistema"),)
    except ObjectDoesNotExist:
        TwoStepsAuth.objects.get(user = u).delete()
        token = Token.objects.create(user = u)
        
def check_if_user_exists(user):
    u = User.objects.get(pk = user.pk)
    return u

def check_if_user_exists_email(email):
    u = User.objects.get(email = email)
    return u

    
