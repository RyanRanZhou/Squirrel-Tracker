# Generated by Django 3.2 on 2021-04-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20210409_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='above_ground',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]