from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(max_length="100", blank=True)
    avatar_url = models.URLField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()