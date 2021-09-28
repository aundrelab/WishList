from django.db import models

# Create your models here.

class users(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username