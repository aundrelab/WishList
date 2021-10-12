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

from rest_framework.authtoken.models import Token
from . models import User
import json


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

def about(request):
    return HttpResponse('<h1>The about page</h1>')

@api_view(['PUT',])
def createaccount_view(request):
    # check request data
    serializer = CreateAccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        # if User.objects.filter(username=user.username).exists():
        #     return Response({'username':'username already exists'})
        data['response'] = 'successfully created account'
        data['userId'] = user.userId
        data['name'] = user.name
        data['username'] = user.username
    else:
        data = serializer.errors

    return Response(data)

@api_view(['POST',])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        print('something')
        if serializer.check():
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
        del request.session['username']
        del request.session['password']
        data['success'] = 'successfully logged out user'
    else:
        data = serializer.errors
    return Response(data)


@api_view(['GET'])
def admin_get_all_users(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = CreateAccountSerializer(user, many=True)
        json_obj = json.dumps(serializer.data)
        print(json_obj)
        return Response(serializer.data)

@api_view(['PUT', 'GET'])
def updateUser(request, userId):
    try:
        item = User.objects.get(userId=userId)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = CreateAccountSerializer(item)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)