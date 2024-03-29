#Python libraries
import re

class Parser:
    """Contain methods that clean string variable and get the information we want to send to Google and Wikipedia API"""



    def clean_accent(self, message):
        """Replace all the accent with the right letter in the message and return the message
        
        message : string"""
        #méthode translate
        accent_dict = {
            "a" : ["à", "â", "ä"],
            "e" : ["é", "è", "ê", "ë"],
            "i" : ["î", "ï"],
            "o" : ["ö", "ô"],
            "u" : ["û", "ü", "ù"]
        }

        #For each accent we replace it by the corresponding letter in the message
        for letter, list_accent in accent_dict.items():
            for accent_letter in list_accent:
                message = message.replace(accent_letter, letter)

        return message

    
    
    def clean_special_character(self, message):
        """Clean a string by suppressing the characters (,;:!./§?-_çà and accent) and return the message
        
        message : string"""

        #We look for the characters we want to delete from the message
        for wrong_char in [",", ";", ".", ":", "/", "!", "?", ".", "\\", "{", "}", "-", "_", "*", "|", "(", ")", "[", "]", "#", "&", "^", "=", "+", "'", "\""]:
            message = message.replace(wrong_char, " ")

        #We delete multiple spaces
        message = re.sub(' +', ' ', message)

        #We delete the space at the last character if it exists
        if message[-1] == " ":
            message = message[:len(message)-1]

        return message



    def clean_message(self, message):
        """Clean the message by lowering its characters, deleting the accent and special characters.
        
        message : string"""

        message = message.lower()
        message = self.clean_accent(message)
        message = self.clean_special_character(message)

        return message

    

    def parse_message(self, message):
        """Parse the message to only get an information about the location and return it
        
        message : string"""

        check_phrase = r"(adresse de|ou se trouve|informations sur|comment se rendre a|parle moi de|ou est|ou se situe) (?P<lieu>[^,.;:?]+)[.,;:?]*"
        message_parsed = re.search(check_phrase, message)

        if message_parsed is not None:
            message = message_parsed.group("lieu")
            return message
            
        else:
            return None

