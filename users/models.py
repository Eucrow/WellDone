# import json
# import pika
# from django.db.models.signals import post_save, pre_delete
# from django.dispatch import receiver
# from django.conf import settings
#
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#         channel = connection.channel()
#         channel.queue_declare(queue='user_admin')
#         event = {
#             "type": "create",
#             "id": instance.id
#         }
#         channel.basic_publish(exchange='',
#                               routing_key='user_admin',
#                               body=json.dumps(event))
#         connection.close()
#
# # @receiver(post_save, sender=User)
# # def save_user_profile(sender, instance, **kwargs):
# #     instance.profile.save()
#
# @receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
# def delete_user_profile(sender, instance, using, **kwargs):
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='user_admin')
#     event = {
#         "type": "delete",
#         "id": instance.id
#     }
#     channel.basic_publish(exchange='',
#                           routing_key='user_admin',
#                           body=json.dumps(event))
#     connection.close()

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    url = models.URLField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
