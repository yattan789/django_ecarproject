# Generated by Django 3.1.2 on 2021-06-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='car_number',
            field=models.CharField(default='xx90', max_length=4),
        ),
        migrations.AddField(
            model_name='product',
            name='company_name',
            field=models.CharField(default='Null', help_text='Maruti,Hundai,etc', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='car',
            field=models.CharField(default='Yes', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Null', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='totalprice',
            field=models.FloatField(default=0.0),
        ),
    ]
