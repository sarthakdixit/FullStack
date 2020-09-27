from djongo import models

# Create your models here.
class Users(models.Model):
  email = models.CharField(max_length=30, primary_key=True)
  password = models.CharField(max_length=100)
  online = models.CharField(max_length=1, default='F')
  verified = models.CharField(max_length=1, default='F')