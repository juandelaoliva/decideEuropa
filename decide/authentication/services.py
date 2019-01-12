from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError
from authentication.models import TwoStepsAuth, UserStatus
from django.core.exceptions import ObjectDoesNotExist
from Crypto import Random
from rest_framework.authtoken.models import Token
from authentication.exceptions import IllegalArgumentException
from django.contrib.auth.hashers import make_password

def send_mail_2_steps_auth(username, password, session_token):
    u = check_if_user_exists_account(username, password)
    check_user_status(u, ['ACTIVE'])
    if not session_token == None: 
        raise IllegalArgumentException(_("The user is already logged"),)
    code = str(int.from_bytes(Random.new().read(24), 'big'))
    try:	
        old_two_steps_auth = TwoStepsAuth.objects.get(user = u)
        old_two_steps_auth.delete()
        two_steps_auth = TwoStepsAuth.objects.create(code = code, user = u)
    except ObjectDoesNotExist:
        two_steps_auth = TwoStepsAuth.objects.create(code = code, user = u)
    return two_steps_auth

def login_email_auth(username, password, code, session_token):
    u = check_if_user_exists_account(username, password)
    check_user_status(u, ['ACTIVE'])
    token = None
    if not session_token == None: 
        raise IllegalArgumentException(_("The user is already logged"),)
    else:
        try:
            token = Token.objects.get(user = u).delete()
        except ObjectDoesNotExist:
            pass
        TwoStepsAuth.objects.get(user = u, code = code).delete()
        token = Token.objects.create(user = u)
    return token
        
def activate_account_recently_registered(username, password, code):
    u = check_if_user_exists_account(username, password)
    check_user_status(u, ['RECENTLY_REGISTERED'])
    TwoStepsAuth.objects.get(user = u, code = code).delete()
    user_status = UserStatus.objects.get(user = u)
    user_status.status = 'ACTIVE'
    user_status.save()
    
def register_user(username, password, email, first_name, last_name):
    hashed_password = make_password(password)
    user = User.objects.create(
        username = username,
        password = hashed_password,
        email = email,
        first_name = first_name,
        last_name = last_name
    )
    user_status = UserStatus.objects.create(status = 'RECENTLY_REGISTERED', user = user)
    code = str(int.from_bytes(Random.new().read(24), 'big'))
    two_steps_auth = TwoStepsAuth.objects.create(user = user, code = code)
    return two_steps_auth

def check_if_user_exists(user):
    u = User.objects.get(pk = user.pk)
    return u

def check_if_user_exists_email(email):
    u = User.objects.get(email = email)
    return u

def check_if_user_exists_account(username, password):
    u = search_user_by_username_and_password(username, password)
    return u

def check_user_status(user, list_status_allowed):
    user_status = UserStatus.objects.get(user = user)
    if not user_status.status in list_status_allowed:
        raise IllegalArgumentException(_("The user can't access this resource"),)

def search_user_by_username_and_password(username, password):
    user = User.objects.get(username = username)
    salt = user.password.split('$')[2]
    hashed_password = make_password(password, salt = salt)
    if not hashed_password == user.password:
        raise ObjectDoesNotExist
    return user


    
