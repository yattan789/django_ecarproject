# Generated by Django 3.1.2 on 2021-05-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210519_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='customer',
            field=models.CharField(default='Null', max_length=20),
        ),
    ]
