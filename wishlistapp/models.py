from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=60)
    username = models.CharField('Username', max_length=60)
    password = models.CharField('Password', max_length=60)

    def set_username(self, username):
        self.username = username

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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)