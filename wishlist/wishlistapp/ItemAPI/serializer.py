from rest_framework import serializers
from rest_framework.views import APIView
from wishlist.wishlistapp.models import User
from wishlist.wishlistapp.models import List
from wishlist.wishlistapp.models import Item

class ItemSerializer(APIView):
    class Meta:
        model = Item
        fields = '__all__';