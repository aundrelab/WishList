from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home of App</h1>');

def about(request):
    return HttpResponse('<h1>The about page</h1>')

# class userList(APIView):
#     def get(self, request):
#         users1 = users.objects.all()
#         serializer = userSerializer(users1, many=True)
#         return Response(serializer.data)