# Generated by Django 4.2.5 on 2023-12-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0004_customuser_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
