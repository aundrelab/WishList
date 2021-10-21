from django.urls import path
from . import views as views
from .ItemAPI import views as item_views
from .ListAPI import views as list_views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('login', views.login, name='app-login'),
    path('signup', views.signup, name='app-signup'),
    path('newItem', views.newItem, name='app-newItem'),
    path('newList', views.newList, name='app-newList'),
    path('about', views.about, name='app-about'),

    # Admin features
    path('getAllUsers/', views.admin_get_all_users, name='getAllUsers'),
    path('<userId>/update-user/', views.updateUser, name="updateUser"),
    path('<userId>/delete-user/', views.deleteUser, name="deleteUser"),

    # Item Features
    path('<itemId>/update-item/', item_views.update, name="update"),
    path('<itemId>/delete-item/', item_views.delete, name="delete"),
    path('<listId>/get-items/', item_views.getItemsofList, name="get"),
    path('<listId>/create-item/', item_views.create, name="create"),

    # List Features
    path('<userId>/create-list/', list_views.create, name="create"),
    path('<userId>/get-lists/', list_views.getListsOfUser, name='get'),

    path('createaccount/', views.createaccount_view, name='app-createaccount'),

    path('deleteaccount/', views.deleteaccount_view, name='app-deleteaccount'),
    path('login/', views.login_view, name='app-login'),
    path('logout/', views.logout_view, name='app-logout'),
]
