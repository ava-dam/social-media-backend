# Generated by Django 3.1.1 on 2020-11-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environments', '0002_auto_20201103_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environments',
            name='Name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]