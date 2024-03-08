from . import views
from django.urls import path
from .views import Events, event_detail

urlpatterns = [
  path('', Events.as_view(), name='events'),
  path('<slug:slug>/', views.event_detail, name='event_detail'),
  path('<slug:slug>/edit_review/<int:review_id>', views.review_edit, name='review_edit')
]