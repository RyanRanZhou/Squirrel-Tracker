from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Count
from .models import Sighting
from django.shortcuts import get_object_or_404
from .forms import AddSightingForm, UpdateSightingForm
from django.http import HttpResponse,JsonResponse

def home(request):

    return render(request, 'tracker/home.html', {})


class MapView(TemplateView):
    template_name = "tracker/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sightings'] = Sighting.objects.all()[:100]
        return context


class ListView(TemplateView):
    template_name = 'tracker/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sightings'] = Sighting.objects.all().order_by('-date')
        return context


def add(request):
    context = {}
    form = AddSightingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Sighting Saved!")
    context['form'] = form
    return render(request, 'tracker/add.html', context)


def detail(request, squirrel_id):
    sighting = get_object_or_404(Sighting, pk = squirrel_id)
    context = {
            'sighting':sighting,
    }
    return render(request, 'tracker/detail.html', context)

def update(request, squirrel_id):
    sighting = get_object_or_404(Sighting, pk = squirrel_id)
    form = UpdateSightingForm(request.POST or None, instance = sighting)
    if form.is_valid():
        form.save()
        return HttpResponse('Update Saved!')
    context = {
            'form': form,
            'sighting': sighting,
    }
    return render(request, 'tracker/update.html', context)

class StatsView(TemplateView):
    template_name = 'tracker/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hectare_stats'] = Sighting.objects.values(
            'hectare').annotate(Count('count'))
        
        age_stats = Sighting.objects.values('age').annotate(Count('count'))
        total = sum([stat['count__count'] for stat in Sighting.objects.values('hectare').annotate(Count('count'))])
        context['age_stats'] = {
            'adult': age_stats.get(age='Adult')['count__count'] / total * 100 // 1,
            'juvenile': age_stats.get(age='Juvenile')['count__count'] / total * 100 // 1
        }

        context['run_stats'] = sum(
            [1 for a in Sighting.objects.filter(running=True)]) / total * 100 // 1
        context['chase_stats'] = sum(
            [1 for a in Sighting.objects.filter(chasing=True)]) / total * 100 // 1
        context['eat_stats'] = sum(
            [1 for a in Sighting.objects.filter(eating=True)]) / total * 100 // 1
        context['climb_stats'] = sum(
            [1 for a in Sighting.objects.filter(climbing=True)]) / total * 100 // 1
        

        return context

