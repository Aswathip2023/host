# Generated by Django 4.1.1 on 2023-04-27 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0002_category_image1_category_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image2',
        ),
    ]
