from django.urls import path, include
from rest_framework import routers
from toyapi.views import ToyViewSet

# URL Configuration
router = routers.DefaultRouter()
router.register('toys', ToyViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
