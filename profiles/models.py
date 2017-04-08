from django.db import models

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def set_password(self, raw_password):
        self.user.set_password(raw_password)

# this is a signal. When a post_save signal is received by model User,
# User's create_user_profile is override by this save_user_profile
# @receiver(post_save, sender=Profile)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=Profile)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()





