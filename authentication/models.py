from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class CustomUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)
    contact = models.CharField(max_length=120)
    
class Forfait(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    date = models.DateTimeField(default=timezone.now)
    offer = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)