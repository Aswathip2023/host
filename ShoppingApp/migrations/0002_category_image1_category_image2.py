# Generated by Django 4.1.1 on 2023-04-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='category'),
        ),
        migrations.AddField(
            model_name='category',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='category'),
        ),
    ]
