from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.sessions.middleware import SessionMiddleware
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from .models import UserFlights
from .forms import FlightsForm
from django.contrib import messages
from django.urls import reverse


def search_flights_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FlightsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            dest_place = form.cleaned_data['dest_place']
            origin_place = form.cleaned_data['origin_place']
            outbound_date = form.cleaned_data['outbound_date']
            inbound_date = form.cleaned_data['inbound_date']
            request.session['dest_place'] = dest_place
            request.session['origin_place'] = origin_place
            request.session['outbound_date'] = outbound_date
            request.session['inbound_date'] = inbound_date
            return HttpResponseRedirect('/result_flights/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = FlightsForm()

    return render(request, 'flights/search_flights.html', {'form': form})


def flights_results_view(request, *args, **kwargs):
    dest_place = request.session.get('dest_place')
    dest = dest_place[-3:]
    origin_place = request.session.get('origin_place')
    origin = origin_place[-3:]
    outbound_date = request.session.get('outbound_date')
    inbound_date = request.session.get('inbound_date')

    if inbound_date:
        url = f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={dest}&departureDate={outbound_date}&returnDate={inbound_date}&adults=1&nonStop=false&max=10'
    else:
        url = f'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin}&destinationLocationCode={dest}&departureDate={outbound_date}&adults=1&nonStop=false&max=10'
    headers = {
        'Authorization': "Bearer iBHDXnvOa3YmE9aApMqlVy66xz2h"
    }
    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.text)

    flights = []
    for flight in results['data']:
        flight_price = flight['price']['total']
        for itineraries in flight['itineraries']:
            flight_dur = itineraries['duration']
            for i, segments in enumerate(itineraries['segments']):
                flights.append(segments['departure']['iataCode'])
                flight_dep_time = segments['departure']['at']
                flight_arr = segments['arrival']['iataCode']
                flight_arr_time = segments['arrival']['at']
                flight_carrier = segments['carrierCode']
                flight_stops = len(itineraries['segments']) - 1

        data = {
            'flight_dep_time': flight_dep_time,
            'flight_arr': flight_arr,
            'flight_arr_time': flight_arr_time,
            'flight_dur': flight_dur,
            'flight_carrier': flight_carrier,
            'flight_price': flight_price,
            'flight_stops': flight_stops,
        }

        flights.append(data)
    print(json.dumps(flights, indent=4, sort_keys=True))
    return render(request, 'flights/result_flights.html', {'results': results, 'outbound_date': outbound_date})


@csrf_exempt
def add_flight(request):
    if request.method == 'POST':
        print(request.POST)
        carrier = request.POST.get('carrier')
        dep_time = request.POST.get('dep-time')
        dep_place = request.POST.get('dep-place')
        flight_time = request.POST.get('flight-time')
        flight_stops = request.POST.get('flight-stops')
        arrival_time = request.POST.get('arrival-time')
        arrival_place = request.POST.get('arrival-place')
        flight_price = request.POST.get('flight-price')
        flight = UserFlights.objects.create(carrier=carrier,
                                            departureDate=dep_time,
                                            departurePlace=dep_place,
                                            duration=flight_time,
                                            stops=flight_stops,
                                            arrivalDate=arrival_time,
                                            arrivalPlace=arrival_place,
                                            price=flight_price,
                                            user=request.user)
        flight.save()
        messages.success(request, f'Your Flight to {arrival_place} has been booked!')
        return JsonResponse({
            'success': True,
            'url': reverse('trips')
        })

