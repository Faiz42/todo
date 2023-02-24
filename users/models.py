from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    name = models.CharField(blank=True, null=True, max_length=255)
    profile_picture = models.FileField(null=True, blank=True, upload_to="profile")
