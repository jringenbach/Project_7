class Parser:
    """Contain methods that clean string variable and get the information we want to send to Google and Wikipedia API"""

    def clean_message(self, message):
        """Clean a string by suppressing the characters (,;:!./§?-_çà and accent)
        
        message : string"""
        return message