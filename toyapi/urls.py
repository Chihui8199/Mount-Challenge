from django.urls import path
from toyapi.views import ToyView

# URL Configuration
urlpatterns = [
    path('toys/', ToyView.as_view()),
    path('toys/<str:name>', ToyView.as_view()),
]
