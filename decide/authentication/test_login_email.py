from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from authentication.services import send_mail_2_steps_auth, login_email_auth
from authentication.models import TwoStepsAuth

from authentication.exceptions import IllegalArgumentException
from django.core.exceptions import ObjectDoesNotExist

class LoginEmailTestCase(TestCase):

    def setUp(self):
        user_test = User.objects.create_user('usertest', 'user@test.com', 'usuarioprueba', first_name = 'User', last_name = 'Test')
        user_test_1 = User.objects.create_user('usertest1', 'user1@test.com', 'usuarioprueba1', first_name = 'User1', last_name = 'Test1')
        TwoStepsAuth.objects.create(user = user_test_1, code = '123456789012345678901234567890123456789013')
        Token.objects.create(user = user_test_1)
        user_test_2 = User.objects.create_user('usertest2', 'user2@test.com', 'usuarioprueba', first_name = 'User2', last_name = 'Test2')
        TwoStepsAuth.objects.create(user = user_test_2, code = '123456789012345678901234567890123456789012')

    def test_send_mail_2_steps_auth(self):
        user = User.objects.get(username = 'usertest')
        two_steps_auth = send_mail_2_steps_auth(user.email)
        db_two_steps_auth = TwoStepsAuth.objects.get(user = user)
        self.assertEqual(two_steps_auth.user, user)
        self.assertEqual(db_two_steps_auth, two_steps_auth)

    # Se pide un código usando un email no registrado en el sistema
    def test_send_mail_2_steps_auth_email_without_user(self):
        res = False
        email = 'email@sin.usuario'
        try:
            two_steps_auth = send_mail_2_steps_auth(email)
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)

    # Se pide un código estando el ususario ya autenticado
    def test_send_mail_2_steps_auth_user_already_authenticated(self):
        res = False
        email = 'user1@test.com'
        try:
            two_steps_auth = send_mail_2_steps_auth(email)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)

    def test_login_email_auth(self):
        email = 'user2@test.com'
        login_email_auth(email)
        user = User.objects.get(email = email)
        try:
            db_token = Token.objects.get(user = user)
            is_created_db_token = True
        except ObjectDoesNotExist:
            is_created_db_token = False
        try:
            db_two_steps_auth = TwoStepsAuth.objects.get(user = user)
            no_two_steps_auth = False
        except ObjectDoesNotExist:
            no_two_steps_auth = True
        self.assertEqual(is_created_db_token, True)
        self.assertEqual(no_two_steps_auth, True)

    # Se hace login usando un email no registrado en el sistema
    def test_login_email_auth_email_without_user(self):
        res = False
        email = 'email@without.user'
        try:
            login_email_auth(email)
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)
    
    # Un usuario que no ha pedido código intenta hacer login
    def test_login_email_auth_user_without_petition(self):
        res = False
        email = 'user@test.com'
        try:
            login_email_auth(email)
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)

    # Un usuario que ya está autenticado intenta hacer login
    def test_login_email_auth_user_already_authenticated(self):
        res = False
        email = 'user1@test.com'
        try:
            login_email_auth(email)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)
