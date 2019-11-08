from grandpy.maps import Maps

def test_maps_get_right_coordinates_from_locations():
    coordinates_to_test = Maps("24 impasse de la Musaraigne").get_coordinates_from_locations()
    results = {
        "lat": 43.6328483,
        "lng": 3.905888
    }
    assert coordinates_to_test == results
