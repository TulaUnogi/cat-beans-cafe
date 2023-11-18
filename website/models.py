from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


CONFIRMATION = ((0, 'Awaiting confirmation'), (1, 'Booking confirmed'), (2, 'Booking declined'))
TABLE_SIZE = ((0, 'Single window seat'), (1, 'Small- 2 seats'), (2, 'Medium- 4 seats'), (3, 'Large- 6 seats'))
TIME_SLOTS = (
    (0, '8:00 - 8:30'),
    (1, '8:30 - 9:00'),
    (2, '9:00 - 9:30'),
    (3, '9:30 - 10:00'),
    (4, '10:00 - 10:30'),
    (5, '10:30 - 11:00'),
    (6, '11:00 - 11:30'),
    (7, '11:30 - 12:00'),
    (8, '12:00 - 12:30'),
    (9, '12:30 - 13:00'),
    (10, '13:00 - 13:30'),
    (11, '13:30 - 14:00'),
    (12, '14:00 - 14:30'),
    (13, '14:30 - 15:00'),
    (17, '15:00 - 15:30'),
    (18, '15:30 - 16:00'),
    (19, '16:00 - 16:30'),
    (20, '16:30 - 17:00')
)


# Extends base User model
class Customer(models.Model):

    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=17, null=True, blank=True)


    def __str__(self):
        if self.user_id:
            return self.phone_number


# Booking model for reservations
class Booking(models.Model):

    booking_customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.IntegerField(choices=TIME_SLOTS, default='8:00', blank=False)
    tables_booked = models.IntegerField(choices=TABLE_SIZE, default=0)
    additional_info = models.TextField(max_length=400, null=True, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.IntegerField(choices=CONFIRMATION, default=0)          


    class Meta:
        ordering = ["booked_on"]
        

    def __str__(self):
        return f'Booking for {self.booking_date} at {self.booking_time} currently has a status: {self.is_confirmed}'
