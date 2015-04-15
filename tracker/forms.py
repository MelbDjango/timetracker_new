from django import forms

from . import models


class EntryForm(forms.ModelForm):

    class Meta:
        model = models.Entry
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data
        if 'start' in data and 'end' in data:
            if data['end']:
                # Ensure end is after start
                if data['start'] > data['end']:
                    # raise forms.ValidationError('Start must be before End')
                    self.add_error('end', 'Start must be before End')
