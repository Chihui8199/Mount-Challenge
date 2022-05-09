from django.urls import path, include
from rest_framework import routers
from toyapi.views import ToyView

# URL Configuration
router = routers.DefaultRouter()
router.register('toys', ToyView)

urlpatterns = [
    path ('api/', include(router.urls))
]
