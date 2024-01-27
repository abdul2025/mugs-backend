# Generated by Django 4.2.5 on 2024-01-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0006_alter_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Regular User'), (0, 'Administrator')], default=1, verbose_name='User Type'),
        ),
    ]
