from django.contrib.auth.models import User
from django.db import models

class LettersDir(models.Model):
    letterdir = models.CharField(max_length=32)

class LettersMessage(models.Model):
    letterauthor = models.OneToOneField(User)
    letterdatacreate = models.DateField(auto_now_add=True)
    # letteradressat = models.OneToOneField(User)
    letterdataopen = models.DateField()
    letterstartdir = models.OneToOneField(LettersDir)

class Mailing(models.Model):
    mailingname = models.CharField(max_length=64)
    mailingadressat = models.OneToOneField(User)

