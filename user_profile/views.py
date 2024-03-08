from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.http import Http404

# Create your views here.

def user_profile(request):
  if request.method == 'POST':
      form = UserProfileForm(request.POST, instance=request.user.userprofile)
      if form.is_valid():
          form.save()
          return redirect('user_profile')
  else:
      form = UserProfileForm(instance=request.user.userprofile)
  return render(request, 'user_profile/user_profile.html', {'form': form})

# @login_required
# def user_profile(request):
#   user = UserProfile.objects.all()
#   try:
#         user_profile = UserProfile.objects.get(user=request.user)
#   except UserProfile.DoesNotExist:
#         raise Http404('User profile not found')
#   return render(request, 'user_profile/user_profile.html', {"user": user})