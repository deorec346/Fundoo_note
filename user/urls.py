from django.urls import path
from django.contrib import admin

from user import views

urlpatterns = [
    path('registration/', views.user_registration, name='registration'),
    path('login/', views.user_login, name='login')
    ]