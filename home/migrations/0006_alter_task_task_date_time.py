# Generated by Django 4.1.7 on 2023-03-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_task_task_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
