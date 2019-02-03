import googlemaps
from datetime import datetime
import json
#Will get API key when needed.
gmaps = googlemaps.Client(key='')
# Geocoding an address
geocode_result = gmaps.geocode('476 5th Ave, New York, NY 10018')
location = geocode_result[0]['geometry']['location']

place_details = gmaps.places(query = '', location = location, radius = 1, type = 'restaurant')

results = []
for i in range(len(place_details['results'])):
    helper = gmaps.distance_matrix(location, place_details['results'][i]['geometry']['location'])
    try:
        result = ((-.5 * place_details['results'][i]['price_level']) + place_details['results'][i]['rating'])/(float(helper['rows'][0]['elements'][0]['distance']['text'].split(' ')[0]))
        results.append((place_details['results'][i]['name'], result))
    except:
        results.append((place_details['results'][i]['name'],0))

print(results)
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                    "Parramatta, NSW",
                                    mode="transit",
                                    departure_time=now)

print("test")
