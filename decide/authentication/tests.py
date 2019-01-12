from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from base import mods


class AuthTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        mods.mock_query(self.client)
        u = User(username='voter1')
        u.set_password('123')
        u.save()

    def tearDown(self):
        self.client = None

    def test_login(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)

        token = response.json()
        self.assertTrue(token.get('token'))

    def test_login_fail(self):
        data = {'username': 'voter1', 'password': '321'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_getuser(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 200)

        user = response.json()
        exists_user = user['id'] > 0 and user != None
        self.assertEqual(exists_user, True)
        self.assertEqual(user['username'], 'voter1')

    def test_getuser_invented_token(self):
        token = {'token': 'invented'}
        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 404)

    def test_getuser_invalid_token(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 1)

        token = response.json()
        self.assertTrue(token.get('token'))

        response = self.client.post('/authentication/logout/', token, format='json')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 404)

    def test_logout(self):
        data = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 1)

        token = response.json()
        self.assertTrue(token.get('token'))

        response = self.client.post('/authentication/logout/', token, format='json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(Token.objects.filter(user__username='voter1').count(), 0)

    def test_register_user_valid(self):
        data = {'first_name': 'voter1', 'last_name': 'voter12', 'email': 'email1@emailcom',
                'username': 'voter1', 'password1': '123', 'password2': '123'
                }
        response = self.client.post('/authentication/register/', data, format='json')
        self.assertEqual(response.status_code,200)
        loginData = {'username': 'voter1', 'password': '123'}
        response = self.client.post('/authentication/login/', loginData, format='json')
        self.assertEqual(response.status_code, 200)
        token = response.json()

        response = self.client.post('/authentication/getuser/', token, format='json')
        self.assertEqual(response.status_code, 200)

        user = response.json()
        self.assertEqual(user['username'], 'voter1')



    def test_register_user_error(self):
        data = {'first_name': 'voter1', 'last_name': 'voter12', 'email': '',
                'username': 'voter1', 'password1': '123', 'password2': '123'
                }
        response = self.client.post('/authentication/register/', data, format='json')
        self.assertEqual(response.status_code,200)
        loginData ={'voter1', '123'}
        response = self.client.post('/authentication/login/', loginData, format='json')
        self.assertEqual(response.status_code, 400)
        token = response.json()

    def test_register_user_error_firt_name(self):
            data = {'first_name': '', 'last_name': 'voter12', 'email': 'email1@email.com',
                    'username': 'voter1', 'password1': '123', 'password2': '123'
                    }
            response = self.client.post('/authentication/register/', data, format='json')
            self.assertEqual(response.status_code, 200)
            loginData = {'voter1', '123'}
            response = self.client.post('/authentication/login/', loginData, format='json')
            self.assertEqual(response.status_code, 400)
            token = response.json()

    def test_register_user_error_last_name(self):
        data = {'first_name': 'voter1', 'last_name': '', 'email': 'email1@email.com',
                'username': 'voter1', 'password1': '123', 'password2': '123'
                }
        response = self.client.post('/authentication/register/', data, format='json')
        self.assertEqual(response.status_code, 200)
        loginData = {'voter1', '123'}
        response = self.client.post('/authentication/login/', loginData, format='json')
        self.assertEqual(response.status_code, 400)
        token = response.json()

    def test_register_user_error_user_name(self):
        data = {'first_name': 'voter1', 'last_name': 'voter12', 'email': 'email1@email.com',
                'username': '', 'password1': '123', 'password2': '123'
                }
        response = self.client.post('/authentication/register/', data, format='json')
        self.assertEqual(response.status_code, 200)
        loginData = {'voter1', '123'}
        response = self.client.post('/authentication/login/', loginData, format='json')
        self.assertEqual(response.status_code, 400)
        token = response.json()
