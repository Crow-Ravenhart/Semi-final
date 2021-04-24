from django.shortcuts import render
from .models import VaccTracker

def home(request):
    trackers = VaccTracker.objects.all()
    return render(request, 'vaccine/home.html', {'trackers':trackers})
