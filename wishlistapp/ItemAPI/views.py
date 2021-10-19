from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from ..models import Item
from ..models import List
from .serializer import ItemSerializer

@api_view(['PATCH', 'GET'])
def update(request, itemId):
    if request.method == 'GET':
        item = Item.objects.get(itemId=itemId)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)

    if request.method == "PATCH":
        item = Item.objects.get(itemId=itemId)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete(request, itemId):
    if request.method == 'GET':
        item = Item.objects.get(itemId=itemId)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)

    if request.method == "DELETE":
        item = Item.objects.get(itemId=itemId)
        item.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


## pass list id to create so item has a list associated to it
@api_view(['POST', 'GET'])
def create(request, listId):
    if request.method == 'GET':
        list_of_item = List.objects.get(listId=listId)
        item = Item(list=list_of_item)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data)

    if request.method == "POST":
        list_of_item = List.objects.get(listId=listId)
        item = Item(list=list_of_item)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getItemsofList(request, listId):
    if request.method == 'GET':
        list = List.objects.get(listId=listId)
        items = Item.objects.filter(list=list)
        serializer = ItemSerializer(items, many=True)
        json1 = json.loads(json.dumps(serializer.data))
        return Response(json1)
