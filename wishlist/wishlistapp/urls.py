from django.urls import path
from . import views
from .ItemAPI import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('delete/<item_id>', views.delete_item, name="delete-item"),
    path('update/<item_id>', views.update_item, name='update-item'),
]
