from rest_framework import serializers
from .models import Toy


class ToySerializer(serializers.ModelSerializer):
    """
          Declare a serializer that we can use to serialize and deserialize data that corresponds to Toy objects
    """

    class Meta:
        model = Toy
        fields = ('id', 'toy_item', 'price')
        lookup_field = 'toy_item'
        extra_kwargs = {
            'url': {'lookup_field': 'toy_item'}
        }
