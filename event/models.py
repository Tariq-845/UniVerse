from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(null=True)
  description = models.TextField()
  image = CloudinaryField('image', default='placeholder')
  date = models.DateTimeField(auto_now_add = True)
  location = models.CharField(max_length=200)
  max_participants = models.IntegerField()
  CHOICES = (
    ('test1', 'test1'),
    ('test2', 'test2'),
    ('test3', 'test3'),
  )
  event_choices = models.CharField(
    max_length=200,
    choices=CHOICES,
    default='test1',
  )



  def __str__(self):
    return self.name
