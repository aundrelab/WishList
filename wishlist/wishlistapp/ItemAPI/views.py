from ..models import Item
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

def update_item(item_id, title, description, category, image_url, item_url):
    item = Item.objects.get(id=item_id)
    item.title = title;
    item.description = description
    item.category = category
    item.imageURL = image_url
    item.itemURL = item_url
    item.save()
    return redirect("url_name")

@api_view(['DELETE'])
def delete(request, item_id):
    Item.objects.get(id=item_id).delete()
    return Response()