import requests
import json



class Wikipedia:
    """Class that handles every action about the wikipedia API"""



    def __init__(self, coordinates):
        """
        self.lng : longitude of the location asked by user (float)
        self.lat : latitude of the location asked by user (float)
        self.pageid : pageid of the wikipedia article (int)
        self.content : content of the wikipedia article (dict)
        """
        self.lng = coordinates["lng"]
        self.lat = coordinates["lat"]
        self.pageid = int()
        self.content = dict()



    def get_pageid_from_coordinates(self):
        """Get a wikipedia pageid from coordinates"""

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

            self.pageid = r_json["query"]["geosearch"][0]["pageid"]

        #If the get request failed
        except:
            print("An error occured while looking for wikipedia url")

    

    def get_content_from_pageid(self):
        """Return the content of a wikipedia page depending on a pageid"""

        params={
            "action" : "query",
            "format" : "json",
            "pageids" : str(self.pageid),
            "prop" : "extracts",
            "explaintext" : "",
            "exlimit" : 1
        }
        url = "https://fr.wikipedia.org/w/api.php"


        try:
            r = requests.get(url, params)
            r_json = r.json()

            self.content = { "title" : r_json["query"]["pages"][str(self.pageid)]["title"],
            "extract" : r_json["query"]["pages"][str(self.pageid)]["extract"]
            }

        except:
            print("Couldn't get content of a page with a pageid")

