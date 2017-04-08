from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Favorites(models.Model):

    fav_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.user.username + ' - ' + self.post.title

