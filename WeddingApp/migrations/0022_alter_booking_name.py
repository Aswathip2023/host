# Generated by Django 4.1.1 on 2023-05-18 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0021_rename_service_booking_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WeddingApp.service'),
        ),
    ]
