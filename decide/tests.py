from django.test import TestCase
from django.conf import settings
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
import subprocess
import os

from base import mods

# Create your tests here.
class BoothTestCase(TestCase):


	def test_ejecutar_without_tests(self):
		cmd = 'python ejecutar.py 0 test'
		returnedValue = subprocess.call(cmd, shell=True)
		
	
		
