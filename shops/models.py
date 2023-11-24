from django.db import models
from uuid import uuid4
from users.models import Profile
# Create your models here.

class Shop(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key = True)
    name = models.TextField()
    thumbnail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class Follower(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
