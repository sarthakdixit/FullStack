from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='user_login'),
    path('registeration/', views.register, name='user_register'),
    path('registeration/registerUser', views.registerUser, name='register_user'),
    path('loginUser', views.loginUser, name='login_user'),
    path('logoutUser', views.logoutUser, name='user_logout'),
    path('back', views.back, name='back'),
]