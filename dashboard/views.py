from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = {}
        return context
