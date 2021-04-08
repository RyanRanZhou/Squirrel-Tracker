from django.urls import path re.path
from .views import MapView, ListView, StatsView
from . import views
urlpatterns = [
    path('', views.home),
    path('map/', MapView.as_view()),
    path('sightings/', ListView.as_view()),
    path('sightings/stats', StatsView.as_view()),
    path('sighting/add', AddView.as_view),
    re.path(r'sightings/(?P<squirrel_id>\d{2}[A-Z]{1}-[A-Z]{2}-\d{4}-\d{2})', views.detail, name='detail')
]

