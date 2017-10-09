import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBhjxBzY5A14d2Q0C_UgGcxpnVpOFZMyyw')

# Geocoding an address
geocode_result = gmaps.geocode('Av Cordoba 111, Ciudad Autonoma de Buenos Aires, Argentina')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((-34.5982940, -58.3699040))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Balcarce 50",
                                     "Ciudad Autonoma de Buenos Aires, ARG",
                                     mode="transit",
                                     departure_time=now)

print("OK!")
print(directions_result)

