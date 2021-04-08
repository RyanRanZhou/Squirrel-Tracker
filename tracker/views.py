from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum, Count
from .models import Sighting
from django.shortcuts import get_object_or_404

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

    return render(request, 'tracker/add.html', {})


def detail(request, squirrel_id):
    squirrel = get_object_or_404(Sighting, pk = squirrel_id)

    context = {
            'squirrel':squirrel,
    }
    return render(request, 'tracker/detail.html', context)

class StatsView(TemplateView):
    template_name = 'tracker/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['hectare_stats'] = Sighting.objects.values(
            'hectare').annotate(Count('count'))

        age_stats = Sighting.objects.values('age').annotate(Count('count'))
        total = sum([stat['count__count'] for stat in age_stats])
        context['age_stats'] = {
            'adult': age_stats[0]['count__count'] / total * 100 // 1,
            'juvenile': age_stats[1]['count__count'] / total * 100 // 1
        }

        context['run_stats'] = sum(
            [a.count for a in Sighting.objects.filter(running=True)]) / total * 100 // 1
        context['chase_stats'] = sum(
            [a.count for a in Sighting.objects.filter(running=True)]) / total * 100 // 1
        context['eat_stats'] = sum(
            [a.count for a in Sighting.objects.filter(running=True)]) / total * 100 // 1
        context['climb_stats'] = sum(
            [a.count for a in Sighting.objects.filter(climbing=True)]) / total * 100 // 1

        context['above_ground_stats'] = '[' + ','.join([
            '[%d, %d]' % (stat['above_ground'], stat['count__count']) for stat in
            Sighting.objects.filter(above_ground__gt=0).values(
                'above_ground').annotate(Count('count'))
        ]) + ']'
        return context

