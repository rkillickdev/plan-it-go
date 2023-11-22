from django.shortcuts import render
from locations.models import Location


def home_view(request):
    destinations = Location.objects.filter(approved=True)
    return render(request, "home/index.html", {"destinations": destinations})
