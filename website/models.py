import datetime
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField
from django.urls import reverse



CONFIRMATION = (
    ('Awaiting confirmation', 'Awaiting confirmation'),
    ('Booking confirmed', 'Booking confirmed'), 
    ('Booking declined', 'Booking declined'),
)
TABLE_SIZE = (('1', 'Single window seat'), ('2', 'Small- 2 seats'), ('4', 'Medium- 4 seats'), ('6', 'Large- 6 seats'))

TIME_SLOTS = (
    ('8:00 - 8:30', '8:00 - 8:30'),
    ('8:30 - 9:00', '8:30 - 9:00'),
    ('9:00 - 9:30', '9:00 - 9:30'),
    ('9:30 - 10:00', '9:30 - 10:00'),
    ('10:00 - 10:30', '10:00 - 10:30'),
    ('10:30 - 11:00', '10:30 - 11:00'),
    ('11:00 - 11:30', '11:00 - 11:30'),
    ('11:30 - 12:00', '11:30 - 12:00'),
    ('12:00 - 12:30', '12:00 - 12:30'),
    ('12:30 - 13:00', '12:30 - 13:00'),
    ('13:00 - 13:30', '13:00 - 13:30'),
    ('13:30 - 14:00', '13:30 - 14:00'),
    ('14:00 - 14:30', '14:00 - 14:30'),
    ('14:30 - 15:00', '14:30 - 15:00'),
    ('15:00 - 15:30', '15:00 - 15:30'),
    ('15:30 - 16:00', '15:30 - 16:00'),
    ('16:00 - 16:30', '16:00 - 16:30'),
    ('16:30 - 17:00', '16:30 - 17:00')
)



class UserProfile(models.Model):
    """
    Extends base User model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(max_length=300)

    def __str__(self):
        if self.user:
            return self.email


# Booking model for reservations
class Booking(models.Model):

    booking_customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    booking_date = models.DateField(default=datetime.date.today)
    booking_time = models.CharField(choices=TIME_SLOTS, default='8:00 - 8:30', max_length=50)
    table_size = models.CharField(choices=TABLE_SIZE, default='1', max_length=50)
    additional_info = models.TextField(max_length=400, null=True, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.CharField(choices=CONFIRMATION, default='Awaiting confirmation', max_length=50)
    slug = AutoSlugField(max_length=70, unique=True, null=True)


    class Meta:
        ordering = ["booked_on"]
        

    def __str__(self):

        return f'Booking for {self.booking_date} at {self.booking_time} was booked on {self.booked_on} and currently has a status: {self.is_confirmed}'

