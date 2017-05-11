from django.contrib.auth.models import User
from django.db import models


class Comentary(models.Model):

    com_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User)
    comentary = models.TextField(max_length=500)
    likes = models.IntegerField(default=0)
    disikes = models.IntegerField(default=0)
    resp_comentary = models.ManyToManyField('self', blank=True)
    create_at = models.DateField(auto_now_add=True)
    modify_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comentary + ' - ' + self.author.username

