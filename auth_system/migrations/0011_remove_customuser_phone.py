# Generated by Django 4.2.5 on 2024-01-23 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0010_customuser_dob_customuser_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='phone',
        ),
    ]
