from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Item
from .serializer import ItemSerializer

@api_view(['PUT',])
def update(request, slug):
    try:
        item = Item.objects.get(slug=slug)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ItemSerializer(item)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def update(request, slug):
    try:
        item = Item.objects.get(slug=slug)
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

# @api_view(['DELETE'])
# def delete(request, item_id):
#     Item.objects.get(id=item_id).delete()
#     return Response()