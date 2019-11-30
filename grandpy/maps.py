import requests
import json

class Maps:



    def __init__(self, message):
        self.message = message



    def get_coordinates_from_locations(self):
        """Get longitude and latitude of a location depending by its name"""

        params = {"address" : self.message, "key" : "AIzaSyDIDOZg2xnz2sAp4wP-1kTDnHwrCZZngTc"}

        try:
            r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=params)
            r_json = r.json()
            print(r_json)
            return r_json["results"][0]["geometry"]["location"]
            
        except Exception as e:
            print(e)