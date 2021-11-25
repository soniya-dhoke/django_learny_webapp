from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from accounts.views import loginUser, registerUser,logoutUser

class TestUrls(SimpleTestCase):

    def test_login_user_url(self):
        url = reverse('login') 
        self.assertEquals(resolve(url).func,loginUser)
    
    def test_most_liked_post_url(self):
        url = reverse('register') 
        self.assertEquals(resolve(url).func,registerUser)

    def test_like_post_url(self):
        url = reverse('logout') 
        self.assertEquals(resolve(url).func,logoutUser)