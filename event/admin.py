from django.contrib import admin
from .models import Event, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
  list_display = ('name', 'slug', 'date')
  search_fields = ['name', 'description']
  list_filter = ('date',)
  prepopulated_fields = {'slug': ('name',)}
  summernote_fields = ('description',)

# Register your models here.
admin.site.register(Review)