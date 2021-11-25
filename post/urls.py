from django.conf.urls import url
from post import views
from django.urls import path 

urlpatterns = [
    path('create/',views.createPost,name='create_post'),
    path('tag/<slug:tag_slug>/',views.search,name='search_by_tag'),
    path('tag/',views.search,name='search'),
    path('most-liked/',views.mostLikedPost,name='most_liked_post'),
    path('newsfeed/',views.mostRecentPost,name='most_recent_post'),
    path('like/',views.likePost,name='like_post'),
]