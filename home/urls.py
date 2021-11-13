from django.conf.urls import url
from home import views
from django.urls import path 

urlpatterns = [
    path('',views.home,name='home'),
]