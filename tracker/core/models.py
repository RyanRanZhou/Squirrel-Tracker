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

    class Shift(models.IntegerChoices):
        A_M_ = 0
        P_M_ = 1

    class Age(models.IntegerChoices):
        ADULT = 0
        JUVENILE = 1
        UNKNOWN = 2

    shift = models.SmallIntegerField(choices=Shift.choices)
    age = models.SmallIntegerField(choices=Age.choices)
