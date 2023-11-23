from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.
GENDER_CHOICES = [(1, 'Male'),(2, 'Female'),(3, 'Other'),]

class Profile(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid4)
    user_auth_id = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length= 200)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
class CreditCard(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4)
    number = models.CharField(max_length=16, null=True, blank=True)
    expiry = models.DateField(null=True, blank=True)
    cvv = models.CharField(max_length=3, null=True, blank=True)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"CreditCard - {self.id}"

class BankAccount(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4)
    fullname = models.CharField(max_length=100, null=True, blank=True)
    id_card = models.CharField(max_length=100, null=True, blank=True)
    name_banking = models.CharField(max_length=100, null=True, blank=True)
    name_branch = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    unsigned_fullname = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self): 
        return f"BankAccount - {self.id}"