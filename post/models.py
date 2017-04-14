from django.contrib.auth.models import User
from django.db import models

from category.models import Category

STATE_POST = (
    ('1', 'BORRADOR'),
    ('2', 'PUBLICADO'),
)

TYPE_POST = (
    ('1', 'PÚBLICO'),
    ('2', 'PRIVADO'),
)


def media_post_path(instance, filename):
    return 'MediaPost/post_{0}_{1}'.format(instance.post_id, filename)


class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=1000)
    content = models.TextField()
    url_media = models.FileField(upload_to=media_post_path, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    publicate_at = models.DateTimeField()
    state = models.CharField(max_length=1, choices=STATE_POST, default='1')
    type = models.CharField(max_length=1, choices=TYPE_POST, default='1')
    author = models.ManyToManyField(User)
    likes = models.IntegerField(default=0)
    post_response = models.OneToOneField("self", null=True, blank=True)
    user_mention = models.ManyToManyField(User, related_name='user_mention', blank=True)
    create_at = models.DateField(auto_now_add=True)
    modify_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.post_id) + ' - ' + self.title
