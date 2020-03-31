from django import forms
from bootstrap_datepicker_plus import DatePickerInput
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class FlightsForm(forms.Form):

    CHOICES = {
        ('return', 'Return'),
        ('oneway', 'One Way')
    }

    return_flight = forms.CharField(widget=forms.Select(attrs={"class": "form-control"}, choices=CHOICES))

    adults = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    origin_place = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    dest_place = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    outbound_date = forms.CharField(
        widget=DatePickerInput(options={'minDate': (datetime.datetime.today() + datetime.timedelta(days=0)).strftime('%Y-%m-%d 00:00:00')}, format='%Y-%m-%d').start_of('flight_date')
    )
    inbound_date = forms.CharField(
        required=False,
        widget=DatePickerInput(format='%Y-%m-%d').end_of('flight_date')
    )
