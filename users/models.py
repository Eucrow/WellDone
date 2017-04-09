from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="profiles/", null=True, blank=True)

    def set_password(self, raw_password):
        self.user.set_password(raw_password)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

# this is a signal. When a post_save signal is received by model User,
# User's create_user_profile is override by this save_user_profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()