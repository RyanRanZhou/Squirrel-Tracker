from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Count

from .models import Sighting

# Create your views here.


class MapView(TemplateView):
    template_name = "map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sightings'] = Sighting.objects.all()[:100]
        return context


class ListView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sightings'] = Sighting.objects.all().order_by('-date')
        return context


