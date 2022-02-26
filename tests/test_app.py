import pytest
import requests
import requests_mock
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


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_get_pokemon(client, requests_mock):
    pokemon_ditto = open(os.path.join('tests', 'pokemon_ditto.json')).read()
    pokemon_species_ditto = open(os.path.join('tests', 'pokemon-species_ditto.json')).read()
    requests_mock.get('https://pokeapi.co/api/v2/pokemon/ditto', text=pokemon_ditto)
    requests_mock.get('https://pokeapi.co/api/v2/pokemon-species/ditto', text=pokemon_species_ditto)

    response = client.get("pokemon/ditto")

    expected_return = {
        "name": "ditto",
        "abilities": ["limber","imposter"],
        "height": 3,
        "weight": 40,
        "types": ["normal"],
        "base_happiness": 50,
        "color": "purple",
        "description": "Capable of copying an enemy's genetic code to instantly transform itself into a duplicate of the enemy.",
        "habitat": "urban",
        "isLegendary": False,
        "isMythical": False
    }

    assert response.json == expected_return

def test_get_pokemon_translated(client, requests_mock):
    pokemon_ditto = open(os.path.join('tests', 'pokemon_ditto.json')).read()
    pokemon_species_ditto = open(os.path.join('tests', 'pokemon-species_ditto.json')).read()
    requests_mock.get('https://pokeapi.co/api/v2/pokemon/ditto', text=pokemon_ditto)
    requests_mock.get('https://pokeapi.co/api/v2/pokemon-species/ditto', text=pokemon_species_ditto)
    
    pokemon_description = "Capable of copying an foe's genetic code to instantly transform itself into a duplicate of the foe."
    shakespeare = requests_mock.post('https://api.funtranslations.com/translate/shakespeare', text=pokemon_description)

    response = client.get("pokemon/translated/ditto")

    assert shakespeare.last_request.json() == {"text": pokemon_description}

    expected_return = {
        "name": "ditto",
        "abilities": ["limber","imposter"],
        "height": 3,
        "weight": 40,
        "types": ["normal"],
        "base_happiness": 50,
        "color": "purple",
        "description": "Capable of copying an foe's genetic code to instantly transform itself into a duplicate of the foe.",
        "habitat": "urban",
        "isLegendary": False,
        "isMythical": False
    }
    assert response.json == expected_return
