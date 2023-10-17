from django.shortcuts import render
from django.views.generic import TemplateView
from locations.models import Location


# class HomeView(TemplateView):
#     """
#     View to render home page
#     """

#     template_name = 'home/index.html'


def home_view(request):

    destinations = Location.objects.all()

    return render(request, 'home/index.html', {"destinations": destinations})
