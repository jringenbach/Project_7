#My own library
from grandpy.parser import Parser
from grandpy.maps import Maps
from grandpy.wikipedia import Wikipedia
from grandpy.grandpytalk import Grandpytalk

#Variable instanciation
parser = Parser()
grandpy = Grandpytalk()
wrong_message = True

#Message told by grandpy and written by user
while wrong_message:
    grandpy.intro_message()
    message = input()

    #Clean the message and getting data
    message = parser.clean_message(message)
    message = parser.parse_message(message)
    wrong_message = True if message == None else False

    if wrong_message:
        grandpy.error_message()