# Generated by Django 3.1.1 on 2020-11-11 20:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environments', '0005_auto_20201111_2156'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userinenv',
            unique_together={('Env_Key', 'User_Key')},
        ),
    ]