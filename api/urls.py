from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
     path('register/', UserRegiserationView.as_view(), name='register'),
     path('login/', UserLoginView.as_view(), name='login')
]