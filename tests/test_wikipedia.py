from grandpy.wikipedia import Wikipedia



def test_get_right_pageid_on_wikipedia_from_coordinates():
    """Test of Wikipedia.get_pageid_from_coordinates()"""
    coord = {'lat': 43.296482, 'lng': 5.36978}
    wiki = Wikipedia(coord)
    wiki.get_pageid_from_coordinates()

    assert wiki.pageid == 5673657