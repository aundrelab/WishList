from django.urls import path
from . import views as views
from .ItemAPI import views as item_views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('<slug>', item_views.update, name="update"),
]
