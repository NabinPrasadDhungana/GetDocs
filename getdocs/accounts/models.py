from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # email, username, first_name, last_name, etc. are included by default
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.png')
    bio = models.TextField(blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    