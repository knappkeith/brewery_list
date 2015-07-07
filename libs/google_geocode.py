import requests

API_KEY = 'AIzaSyCiAGoZ5_J3r6OQqcFS-9xJDgSCUIetFpU'

BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

class Google_Geocode(object):
    def __init__(self):
        self.places = {}

    def add_place(self, place):
        # Check if place exists
        try:
            self.places[place]
        except KeyError:
            self._add_place_dict(place)

    def _add_place_dict(self, place):
        self.places[place] = {}
        api_response = self._get_geocode_response(place)
        this_dict = self.places[place]
        this_dict['search_string'] = place
        this_dict['lng'] = api_response['results'][0]['geometry']['location']['lng']
        this_dict['lat'] = api_response['results'][0]['geometry']['location']['lat']
        this_dict['place_id'] = api_response['results'][0]['place_id']
        this_dict['formatted_address'] = api_response['results'][0]['formatted_address']
        this_dict['google_geocode_response'] = api_response

    def _get_geocode_response(self, place):
        place_str = self._format_string(place)
        params = {'key': API_KEY, 'address': place_str}
        response = requests.get(BASE_URL, params=params)
        self.response = response
        return response.json()

    def _format_string(self, str_to_convert):
        a = str_to_convert.split(" ")
        return "+".join(a)

    def get_lat_lng(self, city):
        place_dict = self._find_dict_entry(city)
        if place_dict == None:
            self.add_place(city)
            place_dict = self._find_dict_entry(city)
        return {'lat': place_dict['lat'], 'lng': place_dict['lng'], 'formatted_address': place_dict['formatted_address']}

    def _find_dict_entry(self, search):
        for i in self.places:
            if i.upper() == search.upper():
                return self.places[i]
            if self.places[i]['formatted_address'] == search:
                return self.places[i]
            if self.places[i]['place_id'] == search:
                return self.places[i]
            if self.places[i]['search_string'] == search:
                return self.places[i]
        return None
