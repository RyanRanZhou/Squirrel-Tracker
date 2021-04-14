# Squirrel_Tracker

## Introduction

This is a Django based web application designed to track all squirrels in the Central Park of New York City.
It allows users to add, update, and view squirrel data.


## Web Path
Home page: https://smiling-audio-307012.df.r.appspot.com	
Map view: https://smiling-audio-307012.df.r.appspot.com/map
All sightings view: https://smiling-audio-307012.df.r.appspot.com/sightings
Add sighting view: https://smiling-audio-307012.df.r.appspot.com/sightings/add
Detail view: https://smiling-audio-307012.df.r.appspot.com/sightings/<unique-squirrel-id>
Update view: https://smiling-audio-307012.df.r.appspot.com/sightings/update/<unique-squirrel-id>
Stats view: https://smiling-audio-307012.df.r.appspot.com/sightings/stats

We apologize that we did not offer a key to home page at each view


## Management Commands

Import: A command that can be used to import the data from the 2018 census file (in CSV format). 
The file path should be specified at the command line after the name of the management command. 
    $ python manage.py import_squirrel_data /path/to/file.csv

Export: A command that can be used to export the data in CSV format. 
The file path should be specified at the command line after the name of the management command. 

    $ python manage.py export_squirrel_data /path/to/file.csv

## Group:

 Project Group 17
 
 Ran Zhou UNI: rz2527
 Jin Shang UNI:
## UNIs:
 
 UNIs: [rz2527,]
