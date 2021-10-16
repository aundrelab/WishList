from rest_framework import serializers
from ..models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["title", "description", "category", "imageURL", "itemURL"]