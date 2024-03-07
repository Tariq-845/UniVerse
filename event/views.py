from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from .models import Event, Review
from .forms import ReviewForm

# Create your views here.
class Events(generic.ListView):
  queryset = Event.objects.all()
  template_name = 'events/events.html'
  paginate_by = 4

def event_detail(request, slug):
  queryset = Event.objects.all()
  event = get_object_or_404(queryset, slug=slug)
  reviews = event.reviews.all().order_by("-date_posted")
  review_count = event.reviews.all().count()

  if request.method == "POST":
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
      review = review_form.save(commit=False)
      review.author = request.user
      review.event = event
      review.save()
      messages.add_message(
        request, messages.SUCCESS,
        'Your review has successfully been posted!'
      )

  review_form = ReviewForm()

  return render(
    request,
    "events/event_detail.html",
    {
      "event": event,
      "reviews": reviews,
      "review_count": review_count,
      "review_form": review_form,
    }
  )
