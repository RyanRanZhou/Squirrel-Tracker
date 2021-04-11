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
                        age = {'Adult': 0, 'Juvenile': 1}[row['Age']]
                    except:
                        age = 2
                    try:
                        above_ground=int(row['Above Ground Sighter Measurement'])
                    except:
                        above_ground=0
                    Sighting(id=row['Unique Squirrel ID'],
                             longitude=row['X'], latitude=row['Y'],
                             date=date(year, month, day),
                             shift={'AM': 0, 'PM': 1}[row['Shift']],
                             age=age,
                             hectare=row['Hectare'],
                             count=row['Hectare Squirrel Number'],
                             running=row['Running'] in ('true', 'TRUE'),
                             chasing=row['Chasing'] in ('true', 'TRUE'),
                             climbing=row['Climbing'] in ('true', 'TRUE'),
                             eating=row['Eating'] in ('true', 'TRUE'),
                             above_ground=above_ground).save()
        except Exception as err:
            raise err
