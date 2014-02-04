from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone

class UserRank(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'UsRank')

    def __unicode__(self):
        return self.name

class UserRights(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'UsRights')

    def __unicode__(self):
        return self.name

class Person(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField(blank=True, null=True)
    mobilenum = models.CharField(max_length=11, blank=True, null=True)
    fromuser = models.CharField(max_length=64, blank=True, null=True)
    userrank = models.ForeignKey(UserRank, related_name='user_rank', verbose_name=u"UserRank", blank=True, null=True)
    userrights = models.ForeignKey(UserRights, related_name='user_rights', verbose_name=u"UserRights",
                                   blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    slogan = models.TextField(blank=True, null=True)