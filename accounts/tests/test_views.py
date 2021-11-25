from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm

class TestViews(TestCase):

    def setUp(self):
        self.client = Client() 
    
    def test_login_user(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/login.html')

    def test_register_user_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'accounts/register.html')


