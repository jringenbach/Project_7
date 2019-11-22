#My own library
from grandpy.parser import Parser
from grandpy.maps import Maps
from grandpy.wikipedia import Wikipedia
from grandpy.grandpytalk import Grandpytalk

#Variable instanciation
parser = Parser()
grandpy = Grandpytalk()
wrong_message = True

#Mettre l'algo dans une fonction

#Message told by grandpy and written by user
while wrong_message:
    grandpy.intro_message()
    message = input()

    #Clean the message
    message = parser.clean_message(message)
    message = parser.parse_message(message)
    wrong_message = True if message == None else False

    if wrong_message:
        grandpy.error_message()

#Getting datas from Google Maps and Wikipedia API
maps = Maps(message)
coordinates = maps.get_coordinates_from_locations()
wiki = Wikipedia(coordinates)
print(wiki.get_url_from_coordinates())

