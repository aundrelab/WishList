from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

from ..models import Item
from ..models import List
from .serializer import ItemSerializer

@api_view(['PUT', 'GET'])
def update(request, itemId):
    try:
        item = Item.objects.get(itemId=itemId)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ItemSerializer(item)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def delete(request, itemId):
    try:
        item = Item.objects.get(itemId=itemId)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = item.delete()
        data = {}
        if operation:
            data["success"] = "update successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)

@api_view(['POST', 'GET'])
def create(request):
    list_of_item = List.objects.get(listId=request.list.listId)
    item = Item(list=list_of_item)

    if request.method == "POST":
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