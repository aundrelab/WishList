from . import views
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from wishlistapp import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('users/', views.userList.as_view()),
]
