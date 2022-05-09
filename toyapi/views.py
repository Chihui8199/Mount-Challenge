from django.shortcuts import render
from .models import Toy
from .serializers import ToySerializer

# third party imports
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework. viewsets import ModelViewSet

class ToyView(APIView):
     #permission_classes = (IsAuthenticated, )

     def get(self, request, name=None):
        # gets toy_item by toy name
        if name:
            toy = get_object_or_404(Toy.objects.all(), toy_item=name)
            serializer = ToySerializer(toy)
            return Response({"Toy": serializer.data},status=status.HTTP_200_OK)

        # gets all toy items
        articles = Toy.objects.all()
        serializer = ToySerializer(articles, many=True)
        return Response({"Toys": serializer.data}, status=status.HTTP_200_OK )

     def post(self, request, *args,  **kwargs):
        serializer = ToySerializer(data=request.data)
        if serializer.is_valid():
            toy_item_saved = serializer.save()
            return Response(
                {"Success": "Toy Item'{}' created successfully".format(toy_item_saved.toy_item)}, status=status.HTTP_200_OK 
                )
        return Response(serializer.errors)

     def delete(self, request, name):
        # Delete toy item by name
        article = get_object_or_404(Toy.objects.all(), toy_item=name)
        article.delete()
        return Response({"message": "Toy with name `{}` has been deleted.".format(name)},status=status.HTTP_204_NO_CONTENT)