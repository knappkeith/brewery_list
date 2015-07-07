from libs.google_geocode import Google_Geocode
from libs.google_place import Google_Place

class Brew_List(dict):
    def __init__(self):
        self.google_geocode = Google_Geocode()
        self.google_place = Google_Place()

    def add_item(self, name, city):
        # see if city is in geocode dict
        self[" - ".join([name, city])] = {}
        cur_brew = self[" - ".join([name, city])]
        lat_lng = self.google_geocode.get_lat_lng(city)
        cur_brew['city_info'] = lat_lng
        cur_brew['place_id'] = self._get_place_id(self._convert_lat_lng_to_str(lat_lng), name)
        details = self.temp_get_details(cur_brew['place_id'])
        self.temp_what_details(cur_brew, details)
        
    def _convert_lat_lng_to_str(self, ll_dict):
        return ",".join([str(ll_dict['lat']), str(ll_dict['lng'])])

    def _get_place_id(self, near, name):
        from_google = self.google_place.search_nearby(near, name)
        return from_google['results'][0]['place_id']

    def temp_get_details(self, id_num):
        return self.google_place.get_details(id_num)


    def temp_what_details(self, current, details):
        try:
            current['url'] = details['result']['url']
        except:
            print "unable to get url"
        try:
            current['formatted_address'] = details['result']['formatted_address']
        except:
            print "unable to get formatted address"
        try:
            current['opening_hours'] = details['result']['opening_hours']['weekday_text']
        except:
            print "unable to get opening hours"
        try:
            current['website'] = details['result']['website']
        except:
            print "unable to get website"
        try:
            current['location'] = details['result']['geometry']['location']
        except:
            print "unable to get location"
        try:
            phone_number = details['result']['formatted_phone_number']
        except:
            print "unable to get phone number"