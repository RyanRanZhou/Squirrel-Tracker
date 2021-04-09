import csv
from datetime import date

from django.core.management.base import BaseCommand
from ...models import Sighting


class Command(BaseCommand):
    help = 'Import squirrel data (csv)'
    output_transaction = True
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument('csv', type=str, help='Path to csv file')

    def handle(self, *args, **kwargs):
        path = kwargs['csv']
        try:
            with open(path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    dt = int(row['Date'])
                    year = dt % 10000
                    month = dt // 1000000
                    day = (dt // 10000) % 100
                    
                    try:
                        age = {'Adult': 'Adult', 'Juvenile': 'Juvenile'}[row['Age']]
                    except:
                        age = 'Unknown'
                    try:
                        if row['Above Ground Sighter Measurement']=='FALSE':
                            above_ground=0
                        else:
                            above_ground=int(row['Above Ground Sighter Measurement'])
                    except:
                        above_ground = None
                    Sighting(squirrel_id=row['Unique Squirrel ID'],
                             longitude=row['X'], latitude=row['Y'],
                             date=date(year, month, day),
                             age=age,
                             location=row['Location'],
                             shift={'AM': 'AM', 'PM': 'PM'}[row['Shift']],
                             hectare=row['Hectare'],
                             count=row['Hectare Squirrel Number'],
                             running=row['Running'] in ('true', 'TRUE'),
                             chasing=row['Chasing'] in ('true', 'TRUE'),
                             climbing=row['Climbing'] in ('true', 'TRUE'),
                             eating=row['Eating'] in ('true', 'TRUE'),
                             foraging=row['Foraging'] in ('true', 'TRUE'),
                             kuks=row['Kuks'] in ('true', 'TRUE'),
                             quaas=row['Quaas'] in ('true', 'TRUE'),
                             moans=row['Moans'] in ('true', 'TRUE'),
                             tail_flags=row['Tail flags'] in ('true', 'TRUE'),
                             tail_twitches=row['Tail twitches'] in ('true', 'TRUE'),
                             approaches=row['Approaches'] in ('true', 'TRUE'),
                             indifferent=row['Indifferent'] in ('true', 'TRUE'),
                             runs_from=row['Runs from'] in ('true', 'TRUE'),
                             primary_fur_color=row['Primary Fur Color'],
                             highlight_fur_color=row['Highlight Fur Color'],
                             combination_color=row['Combination of Primary and Highlight Color'],
                             color_notes=row['Color notes'],
                             specific_location=row['Specific Location'],
                             other_activity=row['Other Activities'],
                             other_interaction=row['Other Interactions'],
                             lat_long=row['Lat/Long'],
                             above_ground=above_ground).save()
        except Exception as err:
            raise err

