from django.shortcuts import render
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

from rest_framework.authtoken.models import Token
from . models import User
import json
import requests


# Create your views here.
def home(request):
    return render(request, 'home.html');

def login(request):
    if request.method == "POST":
        print('inside login')
        req = request.POST
        print(req)
        url = 'http://127.0.0.1:8000/loginendpoint/'
        myobj = {'username': req['username'], 'password': req['password']}
        print(req['username'])
        x = requests.post(url, data=myobj)
        response_data = x.json()
        print(response_data)
        if 'success' in response_data:
            return render(request, 'home.html')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        req = request.POST
        url = 'http://127.0.0.1:8000/createaccount/'
        myobj = {'name': req['name'], 'username': req['username'], 'password': req['password']}
        x = requests.post(url, data=myobj)
        response_data = x.json()
        print(response_data)

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

def newItem(request):
    return render(request, 'newItem.html');

def newList(request):
    return render(request, 'newList.html');

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
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)

@api_view(['GET', 'PATCH'])
def updateUser(request, userId):
    try:
        user = User.objects.get(userId=userId)
        print(user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = User.objects.get(userId=userId)
        print(user)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        user = User.objects.get(userId=userId)
        serializer = UserSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'GET'])
def deleteUser(request, userId):
    try:
        user = User.objects.get(userId=userId)
        print(user)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user = User.objects.get(userId=userId)
        print(user)
        serializer = UserSerializer(user, many=False)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)
    elif request.method == "DELETE":
        operation = user.delete()
        data = {}
        if operation:
            data["success"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data=data)
