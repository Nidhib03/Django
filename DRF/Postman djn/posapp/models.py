# from fileinput import Restfile
from django.db import models
# Create your models here.

class Restfile(models.Model):
  file = models.FileField(blank=False, null=False)
  remark = models.CharField(max_length=20)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  # image= models.ImageField(("Image"),upload_to=upload_to, default='posts/macro-nature.jpg')