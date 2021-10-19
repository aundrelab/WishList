from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import List
from ..models import User
from .serializer import ListSerializer

@api_view(['POST', 'GET'])
def create(request):
    user_of_list = User.objects.get(userId=request.user.userId)
    list = List(user=user_of_list)

    if request.method == "POST":
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)