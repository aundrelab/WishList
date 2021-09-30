from ..models import Item
from django.shortcuts import redirect

def update_item(item_id, title, description, category, image_url, item_url):
    item = Item.objects.get(id=item_id)
    item.title = title;
    item.description = description
    item.category = category
    item.imageURL = image_url
    item.itemURL = item_url
    item.save()
    return redirect("url_name")

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect("list-items")
