from django.db import models

class Urlsdb(models.Model):
    long_url=models.CharField(max_length=10000,blank=False,unique=True)
    short_url=models.CharField(max_length=50,unique=True)
# Create your models here.
