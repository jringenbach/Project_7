import requests
import json

class Maps:



    def __init__(self, message):
        self.message = message



    def get_coordinates_from_locations(self):
        """Get longitude and latitude of a location depending by its name"""

        API_key = self.read_API_Key("api_key_google_maps.txt")
        params = {"address" : self.message, "key" : API_key}

        try:
            r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=params)
            r_json = r.json()
            print(r_json)
            return r_json["results"][0]["geometry"]["location"]
            
        except Exception as e:
            print(e)

    

    def read_API_Key(self, filename):
        """Read the API Key from a file and returns it"""

        with open(filename, "r") as file:
            return file.readline()