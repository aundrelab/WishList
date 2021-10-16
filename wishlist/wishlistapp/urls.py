from django.urls import path
from . import views as views
from .ItemAPI import views as item_views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('<slug>', item_views.update, name="update"),
    path('createaccount/', views.createaccount_view, name='app-createaccount'),
    path('deleteaccount/', views.deleteaccount_view, name='app-deleteaccount'),
]
