from django.db import models

# Create your models here.


class Sighting(models.Model):
    id = models.CharField(max_length=14, primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    date = models.DateField()
    hectare = models.CharField(max_length=3)
    count = models.IntegerField()

    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()

    above_ground = models.IntegerField()

