from django.test import TestCase, Client
from django.urls import reverse
from post.models import Post
from django.contrib.auth.models import User
from taggit.models import Tag

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(
            username = "testuser",
            email = "test@gmail.com",
            password = "testpass",
        )  
        self.test_user.save()  
        self.test_post = Post.objects.create(
            title = "test title",
            tags = [ 'tag1'],
            author = self.test_user
        )
        self.test_post.save()
        self.client.force_login(self.test_user)

    def test_create_post_GET(self):
        response = self.client.get(reverse('create_post'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'post/createPost.html')

    def test_create_post_POST(self):
        response = self.client.post(reverse('create_post'),{
            'title' : "test title2",
            'tags' : [ 'tag1'],
            'author' : self.test_user
        })
        post = Post.objects.filter(title="test title2")
        self.assertEquals(post.count(),1)
        self.assertEquals(response.status_code,302)

    def test_most_liked_post(self):
        response = self.client.get(reverse('most_liked_post'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'post/displayPost.html')

    def test_most_recent_post(self):
        response = self.client.get(reverse('most_recent_post'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'post/displayPost.html')

    def test_search_without_tag_as_parameter(self):
        response = self.client.get(reverse('search'),{
            'search': 'tag1'
        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'post/displayPost.html')

    def test_search_with_tag_as_parameter(self):
        response = self.client.get(reverse('search_by_tag',args=['tag1']))
        self.assertTemplateUsed(response,'post/displayPost.html')
    

    def test_like_post(self):
        response = self.client.post(reverse('like_post'),{
            'post_id': self.test_post.id
        })
        self.assertEquals(response.status_code,200)
