from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=64, default='')
    url = models.CharField(max_length=2048)

    def __unicode__(self):
        return self.name


class Good():
    shop = models.ForeignKey(Shop)
    img = models.CharField(max_length=2048)
    url = models.CharField(max_length=2048)



class Comment(models.Model):
    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=2048)