from django.conf.urls import url
from accounts import views
from django.urls import path 

urlpatterns = [
    path('',views.loginUser,name='login'),
    path('register/',views.registerUser,name='register'),
    path('logout/',views.logoutUser,name='logout'),
]