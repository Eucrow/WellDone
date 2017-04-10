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
    create_at = models.DateField(auto_now_add=True)
    modify_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comentary + ' - ' + self.author.username

    """"
        Método para obtener el número de comentarios de un post
        :param: objeto Post
        :return: numero de comentarios
    """
    def num_post_comentary(self, post):
        num = Comentary.objects.all().select_related('post').filter(post=post).count()
        return num
