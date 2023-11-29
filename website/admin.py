from django.contrib import admin
from .models import Booking, UserProfile
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('booking_customer', 'booking_date', 'booking_time', 'tables_booked', 
    'additional_info', 'booked_on', 'is_confirmed',)
    search_fields = ('booking_customer', 'booking_date',)
    list_filter = ('booking_customer', 'booking_date', 'booking_time','booked_on', 'is_confirmed',)
    summernote_fields = ('additional_info',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email',)
    search_fields = ['last_name', 'phone_number', 'email',]
