from djongo import models

# Create your models here.
class Interior(models.Model):
  owner = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30, default='null')
  email = models.CharField(max_length=30, default='null')
  number = models.CharField(max_length=30, default='null')
  add = models.CharField(max_length=30, default='null')
  city = models.CharField(max_length=30, default='null')
  state = models.CharField(max_length=30, default='null')
  about = models.CharField(max_length=100, default='null')
  date = models.CharField(max_length=15, default='null')
  photo = models.ImageField(upload_to='interior/images')
  video = models.FileField(upload_to='interior/video')

  def __str__(self):
    return self.owner

class Agents(models.Model):
  owner = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30, default='null')
  email = models.CharField(max_length=30, default='null')
  number = models.CharField(max_length=30, default='null')
  add = models.CharField(max_length=30, default='null')
  city = models.CharField(max_length=30, default='null')
  state = models.CharField(max_length=30, default='null')
  about = models.CharField(max_length=100, default='null')
  licence = models.CharField(max_length=15, default='null')
  date = models.CharField(max_length=15, default='null')
  photo = models.ImageField(upload_to='agents')

  def __str__(self):
    return self.owner

class Buildings(models.Model):
  IDNO = models.CharField(max_length=30, primary_key=True)
  typ = models.CharField(max_length=12)
  action = models.CharField(max_length=4)
  localAdd = models.CharField(max_length=30)
  city = models.CharField(max_length=20)
  state = models.CharField(max_length=20)
  pin = models.CharField(max_length=10)
  phone = models.CharField(max_length=10)
  desc = models.CharField(max_length=100)
  neigh = models.CharField(max_length=100)
  area = models.CharField(max_length=20)
  price = models.CharField(max_length=10)
  date = models.CharField(max_length=12, default='null')
  owner = models.CharField(max_length=30, default='Nothing')
  photo1 = models.ImageField(upload_to='buildings/images')
  photo2 = models.ImageField(upload_to='buildings/images')
  photo3 = models.ImageField(upload_to='buildings/images')
  photo4 = models.ImageField(upload_to='buildings/images')
  video = models.FileField(upload_to='buildings/videos')

  def __str__(self):
    return self.IDNO
