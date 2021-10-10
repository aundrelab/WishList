from django.urls import path
from . import views as views
from .ItemAPI import views as item_views

urlpatterns = [
    path('home', views.home, name='app-home'),
    path('login', views.login, name='app-login'),
    path('signup', views.signup, name='app-signup'),
    path('about/', views.about, name='app-about'),
<<<<<<< HEAD
    # path('<slug>', item_views.update, name="update"),
=======

    path('<itemId>/update/', item_views.update, name="update"),
    path('<itemId>/delete/', item_views.delete, name="delete"),
    path('create/', item_views.create, name="create"),

>>>>>>> 915a386f78e8841cb3874e438cc440aa940ebd5f
    path('createaccount/', views.createaccount_view, name='app-createaccount'),
    path('login/', views.login_view, name='app-login'),
]
