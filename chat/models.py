from django.contrib.auth.models import User
from django.db import models


class ChatChannels(models.Model):
    user = models.ForeignKey(User)
    channelname = models.CharField(max_length=24, unique=True)
    channelpassword = models.CharField(max_length=64, blank=True, null=True)


class ChatMessages(models.Model):
    user = models.ForeignKey(User)
    chatchannel = models.ForeignKey(ChatChannels)
    themecreateddata = models.DateField(auto_now_add=True)
    textmessage = models.TextField()


class ChatModerators(models.Model):
    user = models.ForeignKey(User)
    chatchannel = models.ForeignKey(ChatChannels)

class ChatBannedUser(models.Model):
    user = models.ForeignKey(User)
    chatchannel = models.ForeignKey(ChatChannels)
    reason = models.CharField(max_length=256)

class ActiveUsers(models.Model):
    user = models.ForeignKey(User)
    chatchannel = models.ForeignKey(ChatChannels)
