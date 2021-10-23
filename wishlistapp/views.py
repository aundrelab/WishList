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
from .models import List,User,Item
from .ListAPI.serializer import ListSerializer
from .ItemAPI.serializer import ItemSerializer
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
    if request.method == "POST":
        req = request.POST
        url = 'http://127.0.0.1:8000/loginendpoint/'
        myobj = {'username': req['username'], 'password': req['password']}
        x = requests.post(url, data=myobj)
        response_data = x.json()
        if 'success' in response_data:
            user = User.objects.get(username=req['username'])
            request.session['password'] = req['password']
            request.session['username'] = req['username']
            request.session['userId'] = user.userId

            if(request.session['username'] == "admin"):
                return redirect('/admin/home/')

            return redirect('./dashboard')

    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        req = request.POST
        url = 'http://127.0.0.1:8000/createaccount/'
        myobj = {'name': req['name'], 'username': req['username'], 'password': req['password']}
        x = requests.post(url, data=myobj)
        response_data = x.json()
        if 'response' in response_data:
            return render(request, 'login.html')

    return render(request, 'signup.html');


def logout(request):
    req = request.POST
    url = 'http://127.0.0.1:8000/logoutendpoint/'
    myobj = {'username': req['username'], 'password': req['password']}
    x = requests.post(url, data=myobj)
    response_data = x.json()
    return render(request, 'home.html')

def deleteacc(request):
    req = request.DELETE
    url = 'http://127.0.0.1:8000/deleteaccount/'
    myobj = {'username': req['username']}
    x = requests.post(url, data=myobj)
    response_data = x.json()
    return render(request, 'home.html')

def dashboard(request):
    user = User.objects.get(userId=request.session['userId'])
    lists = List.objects.filter(user=user)
    serializer = ListSerializer(lists, many=True)
    json_lists = json.loads(json.dumps(serializer.data))

    json_items_of_list = []
    if len(lists) > 0:
        for list in json_lists:
            id = list['listId']
            list = List.objects.get(listId=id)
            items = Item.objects.filter(list=list)
            serializer = ItemSerializer(items, many=True)
            json_items = json.loads(json.dumps(serializer.data))
            print(json_items)
            json_items_of_list.append(json_items)
    # print('***********************************')
    # print('items of list: ', json_items_of_list)
    # print('lists: ', json_lists)
    return render(request, 'dashboard.html', {'lists': json_lists, 'items': json_items_of_list});

def newItem(request):
    return render(request, 'newItem.html');

def newList(request):
    return render(request, 'newList.html');

def adminHome(request):
    if(request.session['username'] == "admin"):
        return render(request, 'adminHome.html');
    return redirect("../../login")

def adminUsers(request):
    if (request.session['username'] == "admin"):
        response = requests.get('http://127.0.0.1:8000/getAllUsers/').json();
        # pass in users
        my_users = response;
        return render(request, 'userList.html', {'users': my_users});
    return redirect("../../login")

def adminItems(request):
    if(request.session['username'] == "admin"):
        response = requests.get('http://127.0.0.1:8000/getAllItems/').json();
        # pass in items
        my_items = response;
        return render(request, 'itemList.html', {'items': my_items});
    return redirect("../../login")

def adminLists(request):
    if(request.session['username'] == "admin"):
        response = requests.get('http://127.0.0.1:8000/getAllLists/').json();
        # pass in lists
        my_lists = response;
        return render(request, 'allLists.html', {'lists': my_lists});
    return redirect("../../login")

def editItem(request):
    return render(request, 'editItem.html');


def about(request):
    return HttpResponse('<h1>The about page</h1>')

@api_view(['POST',])
def createaccount_view(request):
    # check request data
    serializer = CreateAccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        print('hello')
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
            data['success'] = 'successfully logged in'
        else:
            data = serializer.errors
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST', 'GET'])
def logout_view(request):
    serializer = LogoutSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        del request.session['userId']
        del request.session['username']
        del request.session['password']
        data['success'] = 'successfully logged out user'

    return redirect('../')


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
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def admin_get_all_items(request):
    if request.method == 'GET':
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def admin_get_all_lists(request):
    if request.method == 'GET':
        list = List.objects.all()
        serializer = ListSerializer(list, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def updateUser(request, userId):
    if(request.session['username'] == "admin"):

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
            user = User.objects.get(userId=userId)
            serializer = UserSerializer(user, data=request.data) # FIX
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update successful"
            return redirect('../..')

    return redirect('../../../../login')

@api_view(['GET', 'POST'])
def updateItem(request, title):
    if(request.session['username'] == "admin"):
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
    return redirect('../../../../login')

@api_view(['GET', 'POST'])
def updateList(request, listName):
    if(request.session['username'] == "admin"):
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
            list = List.objects.get(listName=listName)
            serializer = ListSerializer(list, data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "update successful"
            return redirect('../..')
    return redirect('../../../../login')

@api_view(['POST', 'GET'])
def deleteUser(request, userId):
    if(request.session['username'] == "admin"):
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
    return redirect('../../../../login')

@api_view(['POST', 'GET'])
def deleteItem(request, title):
    if(request.session['username'] == "admin"):
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
    return redirect('../../../../login')

@api_view(['POST', 'GET'])
def deleteList(request, listName):
    if(request.session['username'] == "admin"):

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
    return redirect('../../../../login')