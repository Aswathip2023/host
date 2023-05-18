
from django.conf import settings
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
from django.db.models import Count


class register(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True,)
    contact = models.CharField(max_length=12, )
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pincode = models.IntegerField()
    password = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

class Category(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='category')
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='service')
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    description = models.TextField(max_length=250,blank=True)

class Book_status(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Time_slot(models.Model):
    slot = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.slot


# Create An Appointmetment Form
class Booking(models.Model):
    name = models.ForeignKey(Service,on_delete=models.CASCADE,null=True,blank=True)
    contact = models.CharField(max_length=12,null=True,blank=True )
    booking_date = models.DateField(null=True,blank=True)
    booked_on = models.DateField(auto_now=True)
    check_in = models.TimeField(null=True,blank=True)
    check_out = models.TimeField(null=True,blank=True)
    count = models.CharField(max_length=12,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


    # def clean(self):
    #         # count the number of existing appointments for the specified time slot and date
    #         existing_appointments = Booking.objects.filter(
    #             booking_date=self.booking_date,
    #             time_slot=self.time_slot
    #             ).aggregate(num_appointments=Count('id'))['num_appointments']
    #
    #        # limit the number of appointments to 2 per time slot
    #         if existing_appointments >= 2:
    #             raise ValidationError(f"Sorry, the time slot '{self.time_slot}' is already fully booked.")


