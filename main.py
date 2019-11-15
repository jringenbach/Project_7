#My own library
from grandpy.parser import Parser
from grandpy.maps import Maps
from grandpy.wikipedia import Wikipedia
from grandpy.grandpytalk import Grandpytalk

#Variable instanciation
parser = Parser()
grandpy = Grandpytalk()

#Message from grandpy and user
print(grandpy.intro_message())
message = input()


#Clean the message and getting data
parser.clean_message(message)