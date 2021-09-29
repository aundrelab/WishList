from django.contrib import admin
from .models import User
from .models import List
from .models import Item

# Register your models here.

admin.site.register(User)
admin.site.register(List)
admin.site.register(Item)