from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Comentary(models.Model):

    com_id = models.AutoField(primary_key=True)
    author = models.ManyToManyField(User)
    post = models.ManyToManyField(Post)
    comentary = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    disikes = models.IntegerField(default=0)
    resp_comentary = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.author + ' - ' + self.comentary[:30]
