from django.test import TestCase
from accounts.forms import CreateUserForm
from django.contrib.auth.models import User

class TestForms(TestCase):

    def test_user_creation_form(self):
        form = CreateUserForm(data={
                'username' : "testuser",
                'email' : "test@gmail.com",
                'password1' : "msengage",
                'password2' : "msengage",
        })
        self.assertTrue(form.is_valid())

    def test_user_creation_form_invalid_case(self):
        form = CreateUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)