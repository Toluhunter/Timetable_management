from django.views import generic
from django.http import HttpResponse

# Create your views here.
class HomepageView(generic.TemplateView):
    template_name = "index.html"

class AboutPageView(generic.TemplateView):
    template_name = "about.html"

class ConatactPageView(generic.TemplateView):

    template_name = "contact.html"