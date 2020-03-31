from django import forms
from bootstrap_datepicker_plus import DatePickerInput
import datetime
from .models import UserTrips


class UserTripForm(forms.ModelForm):

    class Meta:
        model = UserTrips
        fields = ['travelLocation', 'startDate', 'endDate', 'description', 'totalBudget']

    # travelLocation = forms.CharField(max_length=50)
    # description = forms.CharField(max_length=255)
    # totalBudget = forms.IntegerField()
    # start_date = forms.CharField(
    #     widget=DatePickerInput(
    #         options={'minDate': (datetime.datetime.today() + datetime.timedelta(days=0)).strftime('%Y-%m-%d 00:00:00')},
    #         format='%Y-%m-%d').start_of('travel_date')
    # )
    # end_date = forms.CharField(
    #     required=False,
    #     widget=DatePickerInput(format='%Y-%m-%d').end_of('travel_date')
    # )
