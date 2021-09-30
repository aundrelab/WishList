from ..models import Item

def update_item(item_id, title, description, category, image_url, item_url):
    item = Item.objects.get(item_id)
    item.title = title;
    item.description = description
    item.category = category
    item.imageURL = image_url
    item.itemURL = item_url
    item.save()