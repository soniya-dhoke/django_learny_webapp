from django.test import TestCase
from post.forms import PostCreateForm
from django.contrib.auth.models import User
from taggit.models import Tag

class TestForms(TestCase):

    def test_post_creation_form(self):
        form = PostCreateForm(data={
            'title' : "test title",
            'tags' : [ 'tag1'],
            'author' : User.objects.create(
                username = "test username",
                email = "test@gmail.com",
                password = "testpass",
            )
        })
        self.assertTrue(form.is_valid())

    def test_post_creation_form_invalid_case(self):
        form = PostCreateForm(data={
            'title' : "test title",
            'author' : User.objects.create(
                username = "test username",
                email = "test@gmail.com",
                password = "testpass",
            )
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
