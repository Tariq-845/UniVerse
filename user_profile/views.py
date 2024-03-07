from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import Http404

# Create your views here.
@login_required
def user_profile(request):
  user = UserProfile.objects.all()
  try:
        user_profile = UserProfile.objects.get(user=request.user)
  except UserProfile.DoesNotExist:
        raise Http404('User profile not found')
  return render(request, 'user_profile/user_profile.html', {"user": user})