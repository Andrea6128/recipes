from django import forms

RADIO_CHOICES= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ]

class UserForm(forms.Form):
    radio_button = forms.CharField(label='What is your rating?', widget=forms.RadioSelect(choices=RADIO_CHOICES))

    def __str__(self):
        return self.radio_button
