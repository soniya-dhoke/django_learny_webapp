from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
 
class Post(models.Model):
    title = models.CharField(max_length=100)
    likes = models.ManyToManyField(User,blank=True,default=None,related_name='likes')
    likes_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/',blank=True)
    video = models.FileField(upload_to ='videos/',blank=True)
    content = tinymce_models.HTMLField(blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title