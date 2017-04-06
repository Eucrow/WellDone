from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):

    foll_id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User)
    follower = models.ManyToManyField(User, related_name='followers')

    def __str__(self):
        return self.user.name
