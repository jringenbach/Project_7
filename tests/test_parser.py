from grandpy.parser import Parser

def test_clean_message():
    """Test about the method Parser.clean_message(message)"""

    message = "Je voudrais savoir si c'est possible, d'obtenir les coordonnées et informations sur Paris."
    parser_to_test = Parser()
    message_to_test = parser_to_test.clean_message(message)
    final_message = "je voudrais savoir si c est possible d obtenir les coordonnees et informations sur paris"
    assert message_to_test == final_message