from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Events(TemplateView):
  template_name = 'events.html'
  