from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . serializers import CreateAccountSerializer
from . serializers import LoginSerializer
from . serializers import LogoutSerializer
from . serializers import UserSerializer
from . serializers import ItemSerializer
from . serializers import ListSerializer
from .models import Item, User, List

from rest_framework.authtoken.models import Token

import json
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html');

def login(request):
    print(request.GET);
    return render(request, 'login.html');

def signup(request):
    print(request.POST);
    return render(request, 'signup.html');

def newItem(request):
    return render(request, 'newItem.html');

def newList(request):
    return render(request, 'newList.html');

def adminHome(request):
    #validate admin *WIP*
    return render(request, 'adminHome.html');

def adminUsers(request):
    # Validate admin *WIP*
    response = requests.get('http://127.0.0.1:8000/getAllUsers/').json();
    # pass in users
    my_users = response;
    return render(request, 'userList.html', {'users': my_users});

def adminItems(request):
    # Validate admin *WIP*
    response = requests.get('http://127.0.0.1:8000/getAllItems/').json();
    # pass in items
    my_items = response;
    return render(request, 'itemList.html', {'items': my_items});

def adminLists(request):
    # Validate admin *WIP*
    response = requests.get('http://127.0.0.1:8000/getAllLists/').json();
    # pass in lists
    my_lists = response;
    return render(request, 'allLists.html', {'lists': my_lists});


def about(request):
    return HttpResponse('<h1>The about page</h1>')

@api_view(['POST',])
def createaccount_view(request):
    # check request data
    serializer = CreateAccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'successfully created account'

        data['username'] = user.username
    else:
        data = serializer.errors

    return Response(data)

@api_view(['POST',])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        if serializer.check():
            user = User.objects.get(username=request.data['username'])
            request.session['userId'] = user.userId
            request.session['username'] = request.data['username']
            request.session['password'] = request.data['password']
            data['success'] = 'successfully logged in'
        else:
            data = serializer.errors
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST',])
def logout_view(request):
    serializer = LogoutSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        del request.session['userId']
        del request.session['username']
        del request.session['password']
        data['success'] = 'successfully logged out user'
    else:
        data = serializer.errors
    return Response(data)


@api_view(['DELETE',])
def deleteaccount_view(request):
    try:
        user = User.objects.get(username=request.data['username'])
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    operation = user.delete()
    data = {}
    if operation:
        data['success'] = 'successfully deleted user'
    else:
        data['failure'] = 'failed to delete user'

    return Response(data=data)

@api_view(['GET'])
def admin_get_all_users(request):
    # validate admin *WIP*
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def admin_get_all_items(request):
    # validate admin *WIP*
    if request.method == 'GET':
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def admin_get_all_lists(request):
    # validate admin *WIP*
    if request.method == 'GET':
        list = List.objects.all()
        serializer = ListSerializer(list, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def updateUser(request, userId):
    # validate admin *WIP*
    try:
        user = User.objects.get(userId=userId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        context = {
            "user": user
        }
        return render(request, "userUpdate.html", context)
    elif request.method == 'POST':
        user = User.objects.get(username=user.username)
        serializer = CreateAccountSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
        return redirect('../..')

@api_view(['GET', 'POST'])
def updateItem(request, title):
    # validate admin *WIP*
    try:
        item = Item.objects.get(title=title)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        context = {
            "item": item
        }
        return render(request, "itemUpdate.html", context)
    elif request.method == 'POST':
        item = Item.objects.get(title=title)
        serializer = ItemSerializer(item, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
        return redirect('../..')

@api_view(['GET', 'POST'])
def updateList(request, listName):
    # validate admin *WIP*
    try:
        list = List.objects.get(listName=listName)
    except List.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        context = {
            "list": list
        }
        return render(request, "listUpdate.html", context)
    elif request.method == 'POST':
        print("Here")
        list = List.objects.get(listName=listName)
        serializer = ListSerializer(list, data=request.data)
        print(list)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
        return redirect('../..')

@api_view(['POST', 'GET'])
def deleteUser(request, userId):
    # validate admin *WIP*
    try:
        user = User.objects.get(userId=userId)
        print(user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == "GET"):
        context = {
            "user": user
        }
        return render(request, "userDelete.html", context)
    elif(request.method == "POST"): # Post method for when you delete the user
        user.delete()
        return redirect('../../')

@api_view(['POST', 'GET'])
def deleteItem(request, title):
    # validate admin *WIP*
    try:
        item = Item.objects.get(title=title)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == "GET"):
        context = {
            "item": item
        }
        return render(request, "itemDelete.html", context)
    elif(request.method == "POST"): # Post method for when you delete the user
        item.delete()
        return redirect('../../')

@api_view(['POST', 'GET'])
def deleteList(request, listName):
    # validate admin *WIP*
    try:
        list = List.objects.get(listName=listName)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if (request.method == "GET"):
        context = {
            "list": list
        }
        return render(request, "listDelete.html", context)
    elif(request.method == "POST"): # Post method for when you delete the user
        list.delete()
        return redirect('../../')