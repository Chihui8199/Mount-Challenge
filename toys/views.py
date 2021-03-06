from .models import Toy
from .serializers import ToySerializer

# third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class ToyViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'toy_item'
    serializer_class = ToySerializer
    queryset = Toy.objects.all()
