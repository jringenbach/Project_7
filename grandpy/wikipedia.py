import requests
import json

class Wikipedia:
    """Class that handles every action about the wikipedia API"""

    def __init__(self, keyword):
        self.keyword = keyword

    def get_url_from_keyword(self):
        """Get a wikipedia url from a keyword"""

        params = {"action" : "query" , "format" : "json", "prop" : "info", "generator" : "allpages", "inprop" : "url", "gapfrom" : self.keyword, "aplimit" : 5}
        url = "https://en.wikipedia.org/w/api.php"

        #We try a get request on wikipedia API to get an url depending on the keyword we give in parameters
        try:
            r = requests.get(url, params)
            r_json = r.json()
            url = str()

            i=0
            for page in r_json["query"]["pages"].items():
                if i == 0:
                    url = page[1]["fullurl"]
                    i += 1

            return url

        #If the get request failed
        except:
            print("An error occured while looking for wikipedia url")

wiki = Wikipedia("marseille")
wiki.get_url_from_keyword()