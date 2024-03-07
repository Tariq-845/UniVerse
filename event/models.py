from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(null=True)
  description = models.TextField()
  event_organiser = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="event_names",
    null=True
  )
  image = CloudinaryField('image', default='placeholder')
  date = models.DateTimeField(auto_now_add = True)
  location = models.CharField(max_length=200)
  max_participants = models.IntegerField()
  date_upated = models.DateTimeField(auto_now = True)
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

  class Meta:
    ordering = ["date"]

  def __str__(self):
    return f'{self.name} | hosted by {self.event_organiser}'

class Review(models.Model):
  """ 
  class that stores user reviews
  """
  event = models.ForeignKey(
    Event,
    on_delete=models.CASCADE,
    related_name="reviews"
  )
  author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="review_author"
  )
  body = models.TextField()
  date_posted = models.DateTimeField(auto_now_add = True)

  class Meta:
    ordering = ["date_posted"]

  def __str__(self):
    return f'Review {self.body} by {self.author}'