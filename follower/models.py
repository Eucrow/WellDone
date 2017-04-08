from django.contrib.auth.models import User
from django.db import models


class Follower(models.Model):

    foll_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    follower = models.ForeignKey(User, related_name='u_follower')

    def __str__(self):
        return self.user.username + ' sigue ' + self.follower.username
