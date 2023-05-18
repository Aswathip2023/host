from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Booking, Book_status, Category, Service, Time_slot, Gallery


# Register your models here.



class Time_slotAdmin(admin.ModelAdmin):
    list_display = ('slot', 'status')
    list_editable = ['status']


admin.site.register(Booking)
admin.site.register(Book_status)
admin.site.register(Time_slot, Time_slotAdmin)
admin.site.register(Category)
admin.site.register(Gallery)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'created_at')


admin.site.register(Service, ServiceAdmin)

#
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ("user", "date", "time", "approved")
#     list_filter = ("approved", "date")
#     ordering = ("date", "time")
#     search_fields = ("user_email", "user_name")
