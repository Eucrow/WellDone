from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Favorites(models.Model):

    fav_id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.name

