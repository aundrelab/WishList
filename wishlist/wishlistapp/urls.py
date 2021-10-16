from django.urls import path
from . import views as views
from .ItemAPI import views as item_views
from .ListAPI import views as list_views

urlpatterns = [
    path('home', views.home, name='app-home'),
    path('login', views.login, name='app-login'),
    path('signup', views.signup, name='app-signup'),
    path('newItem', views.newItem, name='app-newItem'),
    path('about/', views.about, name='app-about'),

    path('getAllUsers/', views.admin_get_all_users, name='getAllUsers'),


    path('<userId>/update-user/', views.updateUser, name="updateUser"),
    path('<itemId>/update-item/', item_views.update, name="update"),
    path('<itemId>/delete-item/', item_views.delete, name="delete"),
    path('create-item/', item_views.create, name="create"),

    path('create-list/', list_views.create, name="create"),

    path('createaccount/', views.createaccount_view, name='app-createaccount'),

    path('deleteaccount/', views.deleteaccount_view, name='app-deleteaccount'),
    path('login/', views.login_view, name='app-login'),
    path('logout/', views.logout_view, name='app-logout'),
]
