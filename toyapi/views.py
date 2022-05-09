from django.shortcuts import render
from .models import Toy
from .serializers import ToySerializer

# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework. viewsets import ModelViewSet

class ToyView(ModelViewSet):
   permission_classes = (IsAuthenticated, )
   
   serializer_class = ToySerializer
   queryset = Toy.objects.all()