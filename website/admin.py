from django.contrib import admin
from .models import Booking
from django_summernote.admin  import SummernoteModelAdmin



@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('booking_customer', 'booking_date', 'booking_time', 'tables_booked', 
    'additional_info', 'booked_on', 'is_confirmed',)
    search_fields = ('booking_customer', 'booking_date',)
    list_filter = ('booking_customer', 'booking_date', 'booking_time','booked_on', 'is_confirmed',)
    summernote_fields = ('additional_info',)
