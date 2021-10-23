from django.urls import path
from . import views as views
from .ItemAPI import views as item_views
from .ListAPI import views as list_views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('login', views.login, name='app-login'),
    path('signup', views.signup, name='app-signup'),
    path('dashboard', views.dashboard, name='app-dashboard'),
    path('newItem', item_views.create, name='app-newItem'),
    path('newList', list_views.create, name='app-newList'),
    path('editItem', views.editItem, name='app-editItem'),
    path('about', views.about, name='app-about'),

    # Admin features
    path('getAllUsers/', views.admin_get_all_users, name='getAllUsers'),
    path('getAllItems/', views.admin_get_all_items, name='getAllItems'),
    path('getAllLists/', views.admin_get_all_lists, name='getAllLists'),
    path('admin/home/', views.adminHome, name='adminHome'),
    path('admin/users/', views.adminUsers, name='adminUsers'),
    path('admin/items/', views.adminItems, name='adminItems'),
    path('admin/lists/', views.adminLists, name='adminLists'),
    path('admin/users/<userId>/update-user/', views.updateUser, name="updateUser"),
    path('admin/users/<userId>/delete-user/', views.deleteUser, name="deleteUser"),
    path('admin/items/<title>/update-item/', views.updateItem, name="updateItem"),
    path('admin/items/<title>/delete-item/', views.deleteItem, name="deleteItem"),
    path('admin/lists/<listName>/update-list/', views.updateList, name="updateList"),
    path('admin/lists/<listName>/delete-list/', views.deleteList, name="deleteList"),


    path('<itemId>/update-item/', item_views.update, name="update"),
    path('<itemId>/delete-item/', item_views.delete, name="delete"),
    path('<listId>/get-items/', item_views.getItemsofList, name="get"),
    path('create-item/', item_views.create, name="create"),

    path('<userId>/create-list/', list_views.create, name="create"),

    path('createaccount/', views.createaccount_view, name='app-createaccount'),

    path('deleteaccount/', views.deleteaccount_view, name='app-deleteaccount'),
    path('loginendpoint/', views.login_view, name='app-loginendpoint'),
    path('logoutendpoint/', views.logout_view, name='app-logoutendpoint'),
]
