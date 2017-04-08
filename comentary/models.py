from django.contrib.auth.models import User
from django.db import models

from post.models import Post


class Comentary(models.Model):

    com_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    comentary = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    disikes = models.IntegerField(default=0)
    resp_comentary = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.comentary[:30] + ' - ' + self.author.username
