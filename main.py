#My own library
from grandpy.parser import Parser
from grandpy.maps import Maps
from grandpy.wikipedia import Wikipedia

parser = Parser()
message = "Je test des () et des ||-+ pour la méthode clean_message."
parser.clean_special_character(message)