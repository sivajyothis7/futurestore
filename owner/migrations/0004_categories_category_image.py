# Generated by Django 4.0.6 on 2022-10-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0003_orders_expected_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_image',
            field=models.ImageField(null=True, upload_to='cat_images'),
        ),
    ]
