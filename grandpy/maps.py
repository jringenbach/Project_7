import requests
import json

class Maps:

    def __init__(self, address):
        self.address = address

    def get_coordinates_from_locations(self):
        """Get longitude and latitude of a location depending by its name"""

        params = {"address" : self.address, "key" : "AIzaSyDIDOZg2xnz2sAp4wP-1kTDnHwrCZZngTc"}

        try:
            r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?api=1", params=params)
            r_json = r.json()
            return r_json["results"][0]["geometry"]["location"]
            
        except:
            print("An error occured during the request to google map api")