from django.urls import path
from . import views as views
from .ItemAPI import views as item_views

urlpatterns = [
    path('home', views.home, name='app-home'),
    path('login', views.login, name='app-login'),
    path('signup', views.signup, name='app-signup'),
    path('about/', views.about, name='app-about'),
    path('<slug>', item_views.update, name="update"),
    path('createaccount/', views.createaccount_view, name='app-createaccount'),
]
