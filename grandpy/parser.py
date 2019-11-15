#Python libraries
import re

class Parser:
    """Contain methods that clean string variable and get the information we want to send to Google and Wikipedia API"""



    def clean_special_character(self, message):
        """Clean a string by suppressing the characters (,;:!./§?-_çà and accent)
        
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