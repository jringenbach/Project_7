from grandpy.maps import Maps

class Mock_Request:

    def get(self, url, params=''):
        return 

    def json(self):
        results = {'results': [{'address_components': [{'long_name': '24', 'short_name': '24', 'types': ['street_number']}, {'long_name': 'Impasse de la Musaraigne', 'short_name': 'Impasse de la Musaraigne', 'types': ['route']}, {'long_name': 'Castelnau-le-Lez', 'short_name': 'Castelnau-le-Lez', 'types': ['locality', 'political']}, {'long_name': 'Hérault', 'short_name': 'Hérault', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 
'Occitanie', 'short_name': 'Occitanie', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '34170', 'short_name': '34170', 'types': ['postal_code']}], 'formatted_address': '24 Impasse de la Musaraigne, 34170 Castelnau-le-Lez, France', 'geometry': {'location': {'lat': 43.6328483, 'lng': 3.905888}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 43.6341972802915, 'lng': 3.907236980291502}, 'southwest': {'lat': 43.6314993197085, 'lng': 3.904539019708498}}}, 'place_id': 'ChIJT4_cUF-vthIRIQcci8roRWU', 'plus_code': {'compound_code': 'JWM4+49 Castelnau-le-Lez, France', 'global_code': '8FM5JWM4+49'}, 'types': ['street_address']}], 'status': 'OK'}

        return results

def test_maps_get_right_coordinates_from_locations():

    coordinates_to_test = Maps("24 impasse de la musaraigne").get_coordinates_from_locations()
    results = {
        "lat": 43.6328483,
        "lng": 3.905888
    }

    assert coordinates_to_test == results
