from django.db import models
from django.utils.translation import gettext as _


class Sighting(models.Model):
    squirrel_id = models.CharField(max_length=14, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    date = models.DateField()
    hectare = models.CharField(max_length=3)
    count = models.IntegerField()

    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
    
    

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = [
        (AM, _('AM')),
        (PM, _('PM')),
    ]
    shift = models.CharField(
        choices=SHIFT_CHOICES,
        max_length=5
        )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    UNKNOWN = 'Unknown'
    AGE_CHOICES = [
        (ADULT, _('Adult')),
        (JUVENILE, _('Juvenile')),
        (UNKNOWN, _('Unknown')),
    ]
    age = models.CharField(
        blank = True,
        choices=AGE_CHOICES,
        max_length=10
    )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'
    LOCATION_CHOICES = [
        (ABOVE_GROUND, _('Above Ground')),
        (GROUND_PLANE, _('Ground Plane')),
    ]
    location = models.CharField(
        blank = True,
        choices=LOCATION_CHOICES,
        max_length=15
    )
 
    primary_fur_color = models.CharField(max_length=10, blank=True)
    highlight_fur_color = models.CharField(max_length=50, blank=True)
    combination_color = models.CharField(max_length=50, blank=True)
    color_notes = models.TextField(blank=True)

    
    above_ground_sighter_measurement = models.CharField(max_length=10,blank=True)
    specific_location = models.CharField(max_length=100,blank=True)
    other_activity = models.CharField(max_length=100,blank=True)
    other_interaction = models.CharField(max_length=200,blank=True)
    lat_long = models.CharField(max_length=50)
    
    def __str__(self):
        return self.squirrel_id
