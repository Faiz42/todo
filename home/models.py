from django.db import models

# Create your models here.
from users.forms import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_task")
    task = models.CharField(max_length=255,)
    task_date_time = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)