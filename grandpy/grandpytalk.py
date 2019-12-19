#Python library
import random

#grandpy libraries
from grandpy.parser import Parser
from grandpy.maps import Maps
from grandpy.wikipedia import Wikipedia

class Grandpytalk:



    def intro_message(self):
        """Return a random introduction phrase told by grandpy"""

        liste_intro_phrase = [
            "Que veux-tu savoir mon petit?",
            "Ravi de te voir mon enfant. Je peux t'aider?",
            "J'ai tant de souvenirs à partager, dis-moi ce que tu veux entendre?",
            "Puis-je faire quelque chose pour toi mon petit?",
            "Dans ma folle jeunesse, j'ai visité plein de lieux. Dis-moi le lieu que tu voudrais me voir te raconter!",
            "C'est une belle journée pour te parler du monde, n'est-ce pas? De quoi veux-tu que je te parle?",
            "Tu es venu voir papy pour en savoir plus sur le monde? C'est gentil! :)"
        ]

        return random.choice(liste_intro_phrase)


    def error_message(self):
        """Return a random error message if what the user has written couldn't be parsed"""

        liste_error_phrase = [
            "Je n'ai pas bien compris ta question mon petit. Peux-tu la répéter?",
            "Désolé, je me fais un peu vieux, je n'ai pas bien entendu ta question.",
            "Pardonne mon vieil âge, mais je n'ai pas compris ce que tu m'as dit.",
            "Je n'ai pas entendu ta question, mon enfant. Peux-tu la répéter?",
            "Quelle est ta question? Je n'ai pas bien saisi, pardonne-moi!"
        ]

        return random.choice(liste_error_phrase)


    def ask_grandpy(self, message):
        """Parse and clean the question sent by the user to grandpy
            
        message : string object"""

        grandpy_information = dict()
        parser = Parser()

        #Clean the message
        message = parser.clean_message(message)
        message = parser.parse_message(message)

        #Getting coordinates of location from Google Maps API
        maps = Maps(message)
        coordinates = maps.get_coordinates_from_locations()

        if "error_message" in coordinates.keys():
            return {"error_message" : self.error_message()}

        else:
            grandpy_information.update({"coordinates" : coordinates})

            #Getting information from Wikipedia Page
            wiki = Wikipedia(coordinates)
            wiki.get_pageid_from_coordinates()
            wiki.get_content_from_pageid()   
            grandpy_information.update({"content" : wiki.content})

            return grandpy_information