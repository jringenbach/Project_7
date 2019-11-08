from grandpy.wikipedia import Wikipedia

def test_get_right_url_on_wikipedia_from_keyword():
    wiki = Wikipedia("Marseille")
    url_to_test = wiki.get_url_from_keyword()
    url_expected = "https://en.wikipedia.org/wiki/Marseille"

    assert url_to_test == url_expected