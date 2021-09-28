from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adminLogin(request):
    return HttpResponse('<h1>The login admin page</h1>');

def adminHome(request):
    return HttpResponse('<h1>The home admin page</h1>');

def adminAdd(request):
    return HttpResponse('<h1>The admin add page</h1>');

def adminDelete(request):
    return HttpResponse('<h1>The admin delete page</h1>');

def adminUpdate(request):
    return HttpResponse('<h1>The admin update page</h1>');