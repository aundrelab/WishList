from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . serializers import CreateAccountSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home of App</h1>');

def about(request):
    return HttpResponse('<h1>The about page</h1>')

@api_view(['POST',])
def createaccount_view(request):
    serializer = CreateAccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'successfully registered a new user'
        data['userId'] = user.userId
        data['name'] = user.name
        data['username'] = user.username
        data['password'] = user.password
        token = Token.objects.get(user=user).key
        data['token'] = token
    else:
        data = serializer.errors

    return Response(data)