from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


CONFIRMATION = ((0, 'Awaiting confirmation'), (1, 'Booking confirmed'), (2, 'Booking declined'))
TABLE_SIZE = ((0, 'Single window seat'), (1, 'Small- 2 seats'), (2, 'Medium- 4 seats'), (3, 'Large- 6 seats'))
TIME_SLOTS = (
    ('8:00', '8:00'),
    ('8:30', '8:30'),
    ('9:00', '9:00'),
    ('9:30', '9:30'),
    ('10:00', '10:00'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
)


# Extends base User model
class Customer(models.Model):

    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    contact_phone = models.CharField(max_length=17, null=True, blank=True)
    user_bookings = models.ForeignKey(Bookings, null=True, on_delete=models.CASCADE)


    def __str__(self):
        if self.user_id:
            return f'{self.first_name + " " + self.last_name}'
        else:
            return 'User ID not registered'


# Booking model for reservations
class Bookings(models.Model):
    booking_id = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.CharField(choices=TIME_SLOTS, default='8:00', blank=False)
    tables_booked = models.IntegerField(choices=TABLE_SIZE, default=0)
    additional_info = models.TextField(max_length=400, null=True, blank=True)
    is_confirmed = models.IntegerField(choices=CONFIRMATION, default=0)          


    def __str__(self):
        if self.booking_id:
            return f'Booking for {self.booking_id} currently has a status: {self.is_confirmed}'
        else:
            return 'Booking - User not specified'
