from django.contrib import admin

# Register your models here.
from home.models import Task


@admin.register(Task)
class UserTaskAdmin(admin.ModelAdmin):
    list_display = ["user", "task", "task_date_time", "created", "is_complete"]