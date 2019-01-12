from django.test import TestCase, Client
import random
from base.tests import BaseTestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


from base import mods

# Create your testsfrom django.test import TestCase

class TestBooth(BaseTestCase):
    

    def test_call_view_votings_authenticated(self):
    
        response = self.client.get('/booth/votings/', follow=True) 
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booth/votings.html')

   
