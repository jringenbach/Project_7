import requests
from requests.exceptions import HTTPError
import json
import os

class Maps:



    def __init__(self, message):
        self.message = message



    def get_coordinates_from_locations(self):
        """Get longitude and latitude of a location depending by its name"""

        params = {"address" : self.message, "key" : os.getenv("GOOGLE_MAPS_API_KEY")}
        print(os.getenv("GOOGLE_MAPS_API_KEY"))

        try:
            r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=params)
            r_json = r.json()
            print(r_json)
            if r_json["results"] == []:
                return {"error_message" : ""}
            else:
                return r_json["results"][0]["geometry"]["location"]

        except IndexError:
            print("Error during request : list index out of range")
            return {"error_message" : ""}

        except HTTPError:
            print("Error during request : HTTP error")
            return {"error_message" : ""}           



    def read_API_Key(self, filename):
        """Read the API Key from a file and returns it"""

        with open(filename, "r") as file:
            return file.readline()