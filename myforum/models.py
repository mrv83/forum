from django.contrib.auth.models import User
from django.db import models

class Themes(models.Model):
    nametheme = models.SlugField(max_length=100)
    themetext = models.TextField()
    authuser = models.ForeignKey(User)
    themeclosed = models.BooleanField(default=False)
    themecreateddata = models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.nametheme

class ForumMessages(models.Model):
    messuser = models.ForeignKey(User)
    messtheme = models.ForeignKey(Themes)
    messnum = models.IntegerField()
    messdate = models.DateField(auto_now_add=True)
    messtext = models.TextField()
    messlike = models.IntegerField(blank=True, null=True)
    messdislike = models.IntegerField(blank=True, null=True)
    messvisible = models.BooleanField(default=True)

class IconSmiles(models.Model):
    smileicon = models.ImageField(upload_to='smileicon', max_length=200, blank=True)
    smileview = models.CharField(max_length=10, unique=True)
