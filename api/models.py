from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    image_profile = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=100)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name