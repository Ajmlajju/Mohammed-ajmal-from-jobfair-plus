from django.db import models

# Create your models here.
class regmodel(models.Model):
    username = models.CharField(max_length=25)
    phone = models.IntegerField()
    psw = models.CharField(max_length=20)