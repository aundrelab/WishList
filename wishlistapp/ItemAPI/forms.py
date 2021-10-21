from django import forms
from ..models import Item

class ItemSerializer(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "description", "category", "imageURL", "itemURL"]