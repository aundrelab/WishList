from . import views
from django.urls import path

urlpatterns = [
    path('', views.adminLogin, name='admin-login'),
    path('home/', views.adminHome, name='admin-home'),
    path('add/', views.adminAdd, name='admin-add'),
    path('delete/', views.adminDelete, name='admin-delete'),
    path('update/', views.adminUpdate, name='admin-update'),
]
