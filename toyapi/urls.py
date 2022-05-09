from django.urls import path, include
from rest_framework import routers
from toyapi.views import ToyView
from rest_framework.authtoken.views import obtain_auth_token
from . import views

#URL Configuration
urlpatterns = [
    path('toys/', ToyView.as_view()),
    path('toys/<str:name>', ToyView.as_view()),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
