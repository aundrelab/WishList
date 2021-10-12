from django.urls import path
from . import views as views
from .ItemAPI import views as item_views

urlpatterns = [
    path('home', views.home, name='app-home'),
    path('login', views.login, name='app-login'),
    path('signup', views.signup, name='app-signup'),
    path('newItem', views.newItem, name='app-newItem'),
    path('about/', views.about, name='app-about'),

    path('<itemId>/update/', item_views.update, name="update"),
    path('<itemId>/delete/', item_views.delete, name="delete"),
    path('create/', item_views.create, name="create"),

    path('createaccount/', views.createaccount_view, name='app-createaccount'),
]
