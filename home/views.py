from django.shortcuts import render
from locations.models import Location


def home_view(request):
    """
    View to render the home page and include approved destinations as part
    of the context.
    """
    destinations = Location.objects.filter(approved=True)
    return render(request, "home/index.html", {"destinations": destinations})
