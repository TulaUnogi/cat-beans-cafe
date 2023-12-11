from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_and_edit_profile(sender, instance, created, **kwargs):
    """
    Signal to create or update the user profile. 
    Thanks to my tutors Jason and Oisin.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
