from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Extends base User model
class Customer(models.Model):

    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    contact_phone = models.CharField(max_length=17, null=True, blank=True)
    user_bookings = models.ManyToOneField(Bookings, null=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.user_id:
            return f'{self.first_name + " " + self.last_name}'
        else:
            return 'User ID not registered'