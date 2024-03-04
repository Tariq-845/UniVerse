from . import views
from django.urls import path

urlpatterns = [
  path('events/', views.my_event, name='events')
]