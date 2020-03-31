from django.shortcuts import render, redirect
from .forms import UserTripForm
from .models import UserTrips
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, DetailView
import requests
import json


class TripsDashboard(ListView):
    model = UserTrips

    def get_queryset(self):
        return UserTrips.objects.filter(user=self.request.user)
    template_name = 'trips/trips_dashboard.html'
    context_object_name = 'trips'


class TripDetailView(DetailView):
    model = UserTrips


# @login_required
# def trips_dashboard(request, *args, **kwargs):
#     user = request.user
#     trips = UserTrips.objects.filter(user=user)
#     return render(request, 'trips/trips_dashboard.html', {'trips', trips})


def add_trip(request):
    if request.method == 'POST':
        form = UserTripForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['travelLocation']
            request.session['travelLocation'] = location
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            messages.success(request, f'Your trip has to {trip.travelLocation} been created!')
            return redirect('add_image_url')
    else:
        form = UserTripForm()
    return render(request, 'trips/add_trip.html', {'form': form})


def add_image_url(request):
    location = request.session.get('travelLocation')
    url = f'https://api.unsplash.com/search/photos/?client_id=41ae65cf53ce8f73e9737f6ae3ae9b52d1323df1dbf2ad82283ffa275239b575&query={location}'
    response = requests.request("GET", url)
    results = json.loads(response.text)
    img_url = results['results'][1]['urls']['small']
    trip = UserTrips.objects.latest('user')
    trip.imgUrl = img_url
    trip.save()
    return redirect('dashboard')
