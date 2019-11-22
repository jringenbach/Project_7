from grandpy.wikipedia import Wikipedia

def test_get_right_url_on_wikipedia_from_coordinates():
    coord = {'lat': 43.296482, 'lng': 5.36978}
    wiki = Wikipedia(coord)
    url_to_test = wiki.get_url_from_coordinates()
    url_expected = "https://en.wikipedia.org/wiki/Marseille"

    assert url_to_test == url_expected