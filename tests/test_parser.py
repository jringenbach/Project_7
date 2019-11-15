from grandpy.parser import Parser



def test_clean_accent():
    """Test about the method Parser.clean_accent(message)"""
    message_to_test = "éèêëàâäïîôöûü"
    parser_to_test = Parser()
    message_to_test = parser_to_test.clean_accent(message_to_test)
    final_message = "eeeeaaaiioouu"
    assert message_to_test == final_message


def test_clean_special_character():
    """Test about the method Parser.clean_special_character(message)"""

    message_to_test = "Je voudrais savoir si c'est possible, d'obtenir les coordonnées et informations sur Paris."
    parser_to_test = Parser()
    message_to_test = parser_to_test.clean_special_character(message_to_test)
    final_message = "Je voudrais savoir si c est possible d obtenir les coordonnées et informations sur Paris"
    assert message_to_test == final_message


def test_clean_message():
    """Test the method clean_message from the class Parser"""

    message_to_test = "Je--voudrais\\connaître les Informations sur Parïs+Marseille-Caen."
    parser_to_test = Parser()
    message_to_test = parser_to_test.clean_message(message_to_test)
    final_message = "je voudrais connaitre les informations sur paris marseille caen"
    assert message_to_test == final_message