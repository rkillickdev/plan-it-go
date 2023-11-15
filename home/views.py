from django.shortcuts import render
from locations.models import Location


def home_view(request):
    destinations = Location.objects.all()
    return render(request, "home/index.html", {"destinations": destinations})

def error_404(request):
    return render(request, "404.html")

def error_403(request):
    return render(request, "403.html")

def error_500(request):
    return render(request, "500.html")
