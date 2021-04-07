from django.urls import path
from .views import MapView, ListView, StatsView
urlpatterns = [
    path('map/', MapView.as_view()),
    path('sightings/', ListView.as_view()),
    path('sightings/', StatsView.as_view())
]
