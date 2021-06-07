# Generated by Django 3.1.2 on 2021-06-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20210606_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.CharField(default='Null', help_text='color,condition,past experience,etc', max_length=200),
        ),
    ]