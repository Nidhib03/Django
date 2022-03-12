from unicodedata import name
from xml.parsers.expat import model
from django.db import models

# Create your models here.
class Reapp(models.Model):
    name = models.CharField(max_length=20, blank=False, default='')
    adhar_no = models.IntegerField()
    mail = models.EmailField()
    