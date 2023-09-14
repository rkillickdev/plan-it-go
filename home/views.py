from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    View to render home page
    """

    template_name = 'home/index.html'
