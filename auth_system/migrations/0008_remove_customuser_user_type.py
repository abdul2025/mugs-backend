# Generated by Django 4.2.5 on 2024-01-23 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0007_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
    ]
