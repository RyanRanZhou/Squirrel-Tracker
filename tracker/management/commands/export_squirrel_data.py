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
            with open(path, 'w') as f:
                fieldnames = ['X', 'Y', 'Unique Squirrel ID', 'Hectare', 'Shift', 'Date', 'Hectare Squirrel Number',
                             'Age', 'Primary Fur Color', 'Highlight Fur Color', 'Combination of Primary and Highlight Color',
                             'Color notes', 'Location', 'Above Ground Sighter Measurement', 'Specific Location', 'Running',
                             'Chasing', 'Climbing','Eating','Foraging', 'Other Activities', 'Kuks', 'Quaas', 'Moans', 
                              'Tail flags', 'Tail twitches', 'Approaches', 'Indifferent', 'Runs from', 'Other Interactions',
                             'Lat/Long'
                             ]
                writer = csv.writer(f,delimiter=',')
                writer.writerow(fieldnames)
                fields = Sighting._meta.fields
                for obj in Sighting.objects.all():
                    row = list()
                    for field in fields:
                        row.append(getattr(obj, field.name))
                    writer.writerow(row)
                f.close()
        except Exception as err:
            raise err
