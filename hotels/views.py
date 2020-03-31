from django.shortcuts import render
import requests, json


def search_hotels_view(request, location):

    loc = location[0:3]
    url = f'https://test.api.amadeus.com/v2/shopping/hotel-offers?cityCode={loc}&roomQuantity=1&adults=2&radius=5&radiusUnit=KM&paymentPolicy=NONE&includeClosed=false&bestRateOnly=true&view=FULL&sort=NONE'
    headers = {
        'Authorization': "Bearer BvOz3tfE9OCPw8Wss8M5csPQY6ib"
    }
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)

    hotels = []
    i = 0
    while i < 6:
        hotel_name = results['data'][i]['hotel']['name']
        latitude = results['data'][i]['hotel']['latitude']
        longitude = results['data'][i]['hotel']['longitude']
        self = results['data'][i]['self']

        data = {
            'hotel_name': hotel_name,
            'latitude': latitude,
            'longitude': longitude,
            'image': self
        }
        hotels.append(data)
        i += 1
    return render(request, 'hotels/search_hotels.html', {'results': hotels})
