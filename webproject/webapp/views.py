from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'webapp/home.html'

class AboutView(TemplateView):
    template_name = 'webapp/about.html'

class ResourcesView(TemplateView):
    template_name = 'webapp/resources.html'
