# Generated by Django 4.2 on 2023-04-07 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productbrand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='product_brand_logo'),
        ),
    ]
