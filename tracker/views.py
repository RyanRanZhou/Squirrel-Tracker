from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Count

def maps(request):
    return render(request, 'tracker/maps.html', {})

# Create your views here.
