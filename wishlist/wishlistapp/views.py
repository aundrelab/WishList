from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . serializers import CreateAccountSerializer
from rest_framework.authtoken.models import Token
from . models import User


# Create your views here.
def home(request):
    return render(request, 'home.html');

def login(request):
    return render(request, 'login.html');

def signup(request):
    return render(request, 'signup.html');

def about(request):
    return HttpResponse('<h1>The about page</h1>')

@api_view(['POST',])
def createaccount_view(request):
    serializer = CreateAccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        if User.objects.filter(username=user.username).exists():
            return Response({'username':'username already exists'})
        data['response'] = 'successfully created account'
        data['userId'] = user.userId
        data['name'] = user.name
        data['username'] = user.username

    return Response(data)
#
# @api_view(['POST',])
# def login_view(request):
#     serializer = LoginSerializer(data=request.data)
#     data = {}
#     if serializer.is_valid():
