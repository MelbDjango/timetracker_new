from django import forms

from . import models


class EntryForm(forms.ModelForm):

    class Meta:
        model = models.Entry
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'start': forms.DateTimeInput(attrs={'data-widget': 'picker'}),
        }

    def clean(self):
        data = self.cleaned_data
        if 'start' in data and 'end' in data:
            if data['end']:
                # Ensure end is after start
                if data['start'] > data['end']:
                    self.add_error('end', 'Start must be before End')
