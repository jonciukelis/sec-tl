import requests

class PokeAPI():
    def __init__(self, uri):
        self.uri = uri

    def get_summary(self, pokemon):
        pokemon_details = self.__get_pokemon_details(pokemon)
        pokemon_species_details = self.__get_pokemon_species_details(pokemon)
        return {**pokemon_details, **pokemon_species_details} # Merge responses

    def __get_pokemon_details(self, pokemon):
        url = self.uri + 'pokemon/' + pokemon

        resp_json = _get_json_from_url(url)

        pokemon_details = {}
        pokemon_details['name'] = resp_json['name']

        abilities = []
        for ability in resp_json['abilities']:
            abilities.append(ability['ability']['name'])
        pokemon_details['abilities'] = abilities

        pokemon_details['height'] = resp_json['height']
        pokemon_details['weight'] = resp_json['weight']

        types = []
        for resp_type in resp_json['types']:
            types.append(resp_type['type']['name'])
        pokemon_details['types'] = types

        return pokemon_details

    def __get_pokemon_species_details(self, pokemon):
        url = self.uri + 'pokemon-species/' + pokemon

        resp_json = _get_json_from_url(url)

        pokemon_species_details = {}
        pokemon_species_details['base_happiness'] = resp_json['base_happiness']
        pokemon_species_details['color'] = resp_json['color']['name']

        for entry in resp_json['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                flavor_text = entry['flavor_text']
                # The flavor_text string is dirty
                description = ' '.join(flavor_text.splitlines())
                pokemon_species_details['description'] = description
                break

        pokemon_species_details['habitat'] = resp_json['habitat']['name']
        pokemon_species_details['isLegendary'] = resp_json['is_legendary']
        pokemon_species_details['isMythical'] = resp_json['is_mythical']

        return pokemon_species_details

def _get_json_from_url(url):
    resp = requests.get(url)

    if resp.status_code != requests.codes.ok:
        raise requests.HTTPError('PokeAPI API call to {} returned error {}'.format(url, resp.status_code))

    return resp.json()
