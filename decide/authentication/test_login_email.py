from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .services import send_mail_2_steps_auth, login_email_auth, register_user, activate_account_recently_registered, search_user_by_username_and_password
from .models import TwoStepsAuth, UserStatus
from django.contrib.auth.hashers import make_password

from .exceptions import IllegalArgumentException
from django.core.exceptions import ObjectDoesNotExist

class LoginEmailTestCase(TestCase):

    def setUp(self):
        hashed_password = make_password('usuarioprueba')
        user_test = User.objects.create_user('usertest', 'user@test.com', 'usuarioprueba', first_name = 'User', last_name = 'Test')
        user_status = UserStatus.objects.create(user = user_test, status = 'ACTIVE')
        
        hashed_password_1 = make_password('usuarioprueba1')
        user_test_1 = User.objects.create_user('usertest1', 'user1@test.com', 'usuarioprueba1', first_name = 'User1', last_name = 'Test1')
        user_status_1 = UserStatus.objects.create(user = user_test_1, status = 'ACTIVE')
        two_steps_auth_1 = TwoStepsAuth.objects.create(user = user_test_1, code = '123456789012345678901234567890123456789013')
        Token.objects.create(user = user_test_1)

        hashed_password_2 = make_password('usuarioprueba2')
        user_test_2 = User.objects.create_user('usertest2', 'user2@test.com', 'usuarioprueba2', first_name = 'User2', last_name = 'Test2')
        user_status_2 = UserStatus.objects.create(user = user_test_2, status = 'ACTIVE')
        two_steps_auth_2 = TwoStepsAuth.objects.create(user = user_test_2, code = '123456789012345678901234567890123456789012')
        
        hashed_password_3 = make_password('usuarioprueba3')
        user_test_3 = User.objects.create_user('usertest3', 'user3@test.com', 'usuarioprueba3', first_name = 'User3', last_name = 'Test3')
        user_status_3 = UserStatus.objects.create(user = user_test_3, status = 'RECENTLY_REGISTERED')
        two_steps_auth_3 = TwoStepsAuth.objects.create(user = user_test_3, code = '123456789012345678901234567890123456789019')

    def test_send_mail_2_steps_auth(self):
        user = User.objects.get(username = 'usertest')
        two_steps_auth = send_mail_2_steps_auth(user.username, 'usuarioprueba', None)
        db_two_steps_auth = TwoStepsAuth.objects.get(user = user)
        self.assertEqual(two_steps_auth.user, user)
        self.assertEqual(db_two_steps_auth, two_steps_auth)

    # Se pide un código usando una cuenta de usuario no registrada en el sistema
    def test_send_mail_2_steps_auth_email_without_user(self):
        res = False
        username = 'UsuarioFalso'
        password = 'UsuarioFalso'
        session_token = None
        try:
            two_steps_auth = send_mail_2_steps_auth(username, password, session_token)
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)

    # Se pide un código usando una cuenta de usuario no activada
    def test_send_mail_2_steps_auth_email_account_not_active(self):
        res = False
        user = User.objects.get(username = 'usertest3')
        session_token = None
        try:
            two_steps_auth = send_mail_2_steps_auth(user.username, 'usuarioprueba3', session_token)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)

    # Se pide un código estando el usuario ya autenticado
    def test_send_mail_2_steps_auth_user_already_authenticated(self):
        res = False
        user = User.objects.get(username = 'usertest')
        session_token = 'sessiontoken'
        try:
            two_steps_auth = send_mail_2_steps_auth(user.username, 'usuarioprueba', session_token)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)

    def test_login_email_auth(self):
        user = User.objects.get(username = 'usertest2')
        code = TwoStepsAuth.objects.get(user = user).code
        login_email_auth(user.username, 'usuarioprueba2', code, None)
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

    # Se hace login usando una cuenta de usuario no registrada en el sistema
    def test_login_email_auth_email_without_user(self):
        res = False
        username = 'UsuarioFalso'
        password = 'UsuarioFalso'
        code = '11234567890'
        try:
            login_email_auth(username, password, code, '')
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)
    
    # Se intenta hacer login usando una cuenta de usuario no activada
    def test_login_email_auth_account_not_active(self):
        res = False
        user = User.objects.get(username = 'usertest3')
        code = TwoStepsAuth.objects.get(user = user).code
        session_token = None
        try:
            login_email_auth(user.username, 'usuarioprueba3', code, session_token)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)

    # Un usuario que no ha pedido código intenta hacer login
    def test_login_email_auth_user_without_petition(self):
        res = False
        user = User.objects.get(username = 'usertest')
        session_token = None
        code = ''
        try:
            login_email_auth(user.username, 'usuarioprueba', code, session_token)
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)

    # Un usuario que ya está autenticado intenta hacer login
    def test_login_email_auth_user_already_authenticated(self):
        res = False
        user = User.objects.get(username = 'usertest1')
        code = TwoStepsAuth.objects.get(user = user).code
        session_token = ''
        try:
            login_email_auth(user.username, 'usuarioprueba1', code, session_token)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)

    def test_register_user(self):
        res = False
        username = 'username'
        password = 'password'
        email = 'email'
        first_name = 'firstname'
        last_name = 'lastname'
        register_user(username, password, email, first_name, last_name)
        search_user_by_username_and_password(username, password)

    # Se trata de crear una cuenta sin aportar datos
    def test_register_user_all_blank(self):
        username = ''
        password = ''
        email = ''
        first_name = ''
        last_name = ''
        register_user(username, password, email, first_name, last_name)
 
    # Se trata de activar la cuenta de un usuario que no tiene la correspondiente petición de activacion
    def test_activate_account_recently_registered(self):
        user = User.objects.get(username = 'usertest3')
        code = TwoStepsAuth.objects.get(user = user).code
        activate_account_recently_registered(user.username, 'usuarioprueba3', code)
        try:
            db_two_steps_auth = TwoStepsAuth.objects.get(user = user)
            no_two_steps_auth = False
        except ObjectDoesNotExist:
            no_two_steps_auth = True
        self.assertEqual(no_two_steps_auth, True)

    # Se activa una cuenta de usuario no registrada en el sistema
    def test_activate_account_recently_registered_without_user(self):
        res = False
        username = 'UsuarioFalso'
        password = 'UsuarioFalso'
        code = ''
        try:
            activate_account_recently_registered(username, password, code)
        except ObjectDoesNotExist:
            res = True
        self.assertEqual(res, True)
    
    # Se activa una cuenta de usuario activada
    def test_activate_account_recently_registered_already_active(self):
        res = False
        user = User.objects.get(username = 'usertest2')
        code = TwoStepsAuth.objects.get(user = user).code
        try:
            activate_account_recently_registered(user.username, 'usuarioprueba2', code)
        except IllegalArgumentException:
            res = True
        self.assertEqual(res, True)
        
