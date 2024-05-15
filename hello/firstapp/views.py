from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        context = {
            'message': 'Home page',
            'another_variable': 42,
        }
        return render(request, 'templates/index.html', context)
