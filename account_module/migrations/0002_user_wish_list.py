# Generated by Django 4.2 on 2023-04-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_alter_productbrand_logo'),
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wish_list',
            field=models.ManyToManyField(to='product_module.product'),
        ),
    ]