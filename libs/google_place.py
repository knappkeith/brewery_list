import requests

API_KEY = 'AIzaSyCiAGoZ5_J3r6OQqcFS-9xJDgSCUIetFpU'

BASE_URL = 'https://maps.googleapis.com/maps/api/place/{}/json'

class Google_Place(object):
    def __init__(self):
        self.places = {}

    def get_nearby_search_url(self):
        return BASE_URL.format('nearbysearch')

    def get_details_url(self):
        return BASE_URL.format('details')

    def search_nearby(self, near, name):
        params = {}
        params['key'] = API_KEY
        params['location'] = near
        params['name'] = name
        params['radius'] = 10000
        url = self.get_nearby_search_url()
        response = requests.get(url, params=params)
        return response.json()

    def get_details(self, google_id):
        params = {}
        params['key'] = API_KEY
        params['placeid'] = google_id
        url = self.get_details_url()
        response = requests.get(url, params=params)
        return response.json()