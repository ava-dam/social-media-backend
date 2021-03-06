# Generated by Django 3.1.1 on 2020-11-11 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('environments', '0004_auto_20201111_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinenv',
            name='Env_Key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environments.environments'),
        ),
        migrations.AlterField(
            model_name='userinenv',
            name='User_Key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
