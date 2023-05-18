# Generated by Django 4.1.1 on 2023-05-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0016_remove_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='booking_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='service',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='check_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='check_out',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='contact',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='count',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]