import requests
import json

class Wikipedia:
    """Class that handles every action about the wikipedia API"""

    def __init__(self, coordinates):
        self.lng = coordinates["lng"]
        self.lat = coordinates["lat"]

    def get_url_from_coordinates(self):
        """Get a wikipedia url from a keyword"""
        #geosearch
        #extract : obtenir contenu d'une page wikipedia sans le markup à partir d'une id
        #pageids=0000|plaintext=""
        #prop=info
        params = {"action" : "query" ,
        "format" : "json",
        "list" : "geosearch",
        "gscoord" : str(self.lat)+"|"+str(self.lng),
        "gsradius" : "1000"}
        url = "https://fr.wikipedia.org/w/api.php"

        #We try a get request on wikipedia API to get an url depending on the keyword we give in parameters
        try:
            r = requests.get(url, params)
            r_json = r.json()
            print(r_json)
            url = str()

            return url

        #If the get request failed
        except:
            print("An error occured while looking for wikipedia url")
