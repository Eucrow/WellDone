from django.db import models


class Category(models.Model):

    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
