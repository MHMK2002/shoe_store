# Generated by Django 4.2 on 2023-04-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]