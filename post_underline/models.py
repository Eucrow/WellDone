from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Post_Underline(models.Model):

    pun_id = models.AutoField(primary_key=True)
    post = models.ManyToManyField(Post)
    user = models.ManyToManyField(User)
    # Debe ser la posición inicial y final en la cadena separado por , (122,189)
    content_underline = models.CharField(max_length=100)

    def __str__(self):
        return self.content_underline

