from django import forms
from .models import Sighting


# creating a form
class AddSightingForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Sighting

		# specify fields to be used
		fields = [
			"squirrel_id",
			"longitude",
                        "latitude",
                        "shift",
                        "date",
                        "age",
                        'primary_fur_color',
                        'location',
                        'specific_location',
                        'running',
                        'chasing',
                        'climbing',
                        'eating',
                        'foraging',
                        'other_activity',
                        'kuks',
                        'quaas',
                        'moans',
                        'tail_flags',
                        'tail_twitches',
                        'approaches',
                        'indifferent',
                        'runs_from',
		]

class UpdateSightingForm(forms.ModelForm):
        # create meta class
        class Meta:
                # specify model to be used
                model = Sighting
                # specify fields to be used
                fields = [
                        "squirrel_id",
                        "longitude",
                        "latitude",
                        "shift",
                        "date",
                        "age",
                ]
