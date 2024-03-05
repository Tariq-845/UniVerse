from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  description = models.TextField()
  image = CloudinaryField('image', default='placeholder')
  date = models.DateTimeField(auto_now_add = True)
  location = models.CharField(max_length=200)
  max_participants = models.IntegerField(200)

  def __str__(self):
    return f''
