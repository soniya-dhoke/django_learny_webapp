from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from post.views import createPost,mostLikedPost,mostRecentPost,search,likePost

class TestUrls(SimpleTestCase):

    def test_most_recent_post_url(self):
        url = reverse('most_recent_post') 
        self.assertEquals(resolve(url).func,mostRecentPost)
    
    def test_most_liked_post_url(self):
        url = reverse('most_liked_post') 
        self.assertEquals(resolve(url).func,mostLikedPost)

    def test_like_post_url(self):
        url = reverse('like_post') 
        self.assertEquals(resolve(url).func,likePost)
    
    def test_search_without_tag_url(self):
        url = reverse('search') 
        self.assertEquals(resolve(url).func,search)
    
    def test_search_with_tag_url(self):
        url = reverse('search_by_tag',args=['some-slug']) 
        self.assertEquals(resolve(url).func,search)

    def test_create_post_url(self):
        url = reverse('create_post') 
        self.assertEquals(resolve(url).func,createPost)


    
    