from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from django.shortcuts import render, redirect

from ..models import List
from ..models import User
from .serializer import ListSerializer

@api_view(['POST', 'GET'])
def create(request):
    if request.method == "POST":
        user_of_list = User.objects.get(userId=request.session["userId"])
        list = List(user=user_of_list)

        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('../dashboard')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return render(request, 'newList.html')

@api_view(['POST', 'GET'])
def update(request, listId):
    if request.method == "POST":
        list = List.objects.get(listId=listId)
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('../../dashboard')

    list = List.objects.get(listId=listId)
    serializer = ListSerializer(list)
    json1 = json.loads(json.dumps(serializer.data))
    print(json1)
    return render(request, 'editList.html', {'list': json1})

@api_view(['DELETE', 'GET'])
def delete(request, listId):
    if request.method == 'GET':
        list = List.objects.get(listId=listId)
        list.delete()
        return redirect('../../dashboard')
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getListsOfUser(request):
    if request.method == 'GET':
        user = User.objects.get(userId=request.session['userId'])
        lists = List.objects.filter(user=user)
        serializer = ListSerializer(lists, many=True)
        json1 = json.loads(json.dumps(serializer.data))
        return Response(json1)