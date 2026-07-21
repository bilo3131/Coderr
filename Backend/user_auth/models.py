from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = {
    "business": "Business",
    "customer": "Customer"
}

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    file = models.ImageField(blank=True)
    tel = models.TextField(blank=True)
    location = models.TextField(blank=True)
    description = models.TextField(blank=True)
    working_hours = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=TYPE_CHOICES, default="customer")