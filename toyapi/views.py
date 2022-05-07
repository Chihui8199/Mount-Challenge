from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404

# Third party imports
from .models import Toy
from .serializers import ToySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# TODO: Better design to delete by id instead?

class ToyView(APIView):

     def get(self, request, name=None):
        # Gets toy_item by toy name
        if name:
            toy = get_object_or_404(Toy.objects.all(), toy_item=name)
            #toy = Toy.objects.get()
            serializer = ToySerializer(toy)
            return Response({"Toy": serializer.data})
        # Gets all Toy item
        articles = Toy.objects.all()
        serializer = ToySerializer(articles, many=True)
        return Response({"Toys": serializer.data})

     def post(self, request, *args,  **kwargs):
        serializer = ToySerializer(data=request.data)
        if serializer.is_valid():
            toy_item_saved = serializer.save()
            return Response(
                {"Success": "Toy Item'{}' created successfully".format(toy_item_saved.toy_item)}, status=status.HTTP_200_OK 
                )
        return Response(serializer.errors)

     def delete(self, request, name):
        # Delete object by name
        article = get_object_or_404(Toy.objects.all(), toy_item=name)
        article.delete()
        return Response({"message": "Toy with name `{}` has been deleted.".format(name)},status=status.HTTP_204_NO_CONTENT)