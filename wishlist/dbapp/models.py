from django.db import models

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=60)
    username = models.CharField('Username', max_length=60)
    password = models.CharField('Password', max_length=60)

class List(models.Model):
    listId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    listName = models.CharField('List Name', max_length=60)
    description = models.TextField('Description', blank=True)

class Item(models.Model):
    itemId = models.AutoField(primary_key=True)
    list = models.ForeignKey(List, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=60)
    description = models.CharField('Description', max_length=200)
    category = models.CharField('Category', max_length=60)
    imageURL = models.URLField('Image URL')
    itemURL = models.URLField('Item URL')