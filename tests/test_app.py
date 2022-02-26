import pytest
import requests_mock  # noqa: F401
import json
import os.path
from app import create_app


@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_get_pokemon(client, requests_mock):  # noqa: F811
    pokemon_ditto = open(os.path.join('tests', 'pokemon_ditto.json')).read()
    pokemon_species_ditto = open(os.path.join('tests', 'pokemon-species_ditto.json')).read()
    requests_mock.get('https://pokeapi.co/api/v2/pokemon/ditto', text=pokemon_ditto)
    requests_mock.get(
        'https://pokeapi.co/api/v2/pokemon-species/ditto',
        text=pokemon_species_ditto
    )

    response = client.get("pokemon/ditto")

    assert response.json == {
        "name": "ditto",
        "abilities": ["limber", "imposter"],
        "height": 3,
        "weight": 40,
        "types": ["normal"],
        "base_happiness": 50,
        "color": "purple",
        "description":  "Capable of copying an enemy's genetic code" +
                        " to instantly transform itself into a duplicate of the enemy.",
        "habitat": "urban",
        "isLegendary": False,
        "isMythical": False
    }


def test_get_pokemon_translated(client, requests_mock):  # noqa: F811
    pokemon_ditto = open(os.path.join('tests', 'pokemon_ditto.json')).read()
    pokemon_species_ditto = open(os.path.join('tests', 'pokemon-species_ditto.json')).read()
    requests_mock.get('https://pokeapi.co/api/v2/pokemon/ditto', text=pokemon_ditto)
    requests_mock.get(
        'https://pokeapi.co/api/v2/pokemon-species/ditto',
        text=pokemon_species_ditto
    )

    ditto_shakespeare_response_string = open(
        os.path.join('tests', 'ditto_shakespeare.json')
    ).read()

    shakespeare_mock = requests_mock.post(
        'https://api.funtranslations.com/translate/shakespeare',
        text=ditto_shakespeare_response_string
    )

    ditto_shakespeare_parsed = json.loads(ditto_shakespeare_response_string)['contents']
    ditto_shakespeare_input = ditto_shakespeare_parsed['text']
    ditto_shakespeare_output = ditto_shakespeare_parsed['translated']

    response = client.get("pokemon/translated/ditto")
    assert shakespeare_mock.request_history[0].json()['text'] == ditto_shakespeare_input
    assert response.json == {
        "name": "ditto",
        "abilities": ["limber", "imposter"],
        "height": 3,
        "weight": 40,
        "types": ["normal"],
        "base_happiness": 50,
        "color": "purple",
        "description": ditto_shakespeare_output,
        "habitat": "urban",
        "isLegendary": False,
        "isMythical": False
    }
