from flask import Flask, Response
from pokeapi import PokeAPI
from funtranslations import FunTranslations


def create_app() -> Flask:
    """Create a configured Flash app instance."""
    app = Flask(__name__, instance_relative_config=True)
    app.config['POKEAPI'] = PokeAPI('https://pokeapi.co/api/v2/')
    app.config['FUN_TRANSLATIONS'] = FunTranslations('https://api.funtranslations.com/translate/')

    @app.route('/pokemon/translated/<pokemon_name>')
    def get_pokemon_translated(pokemon_name) -> Response:
        summary = app.config['POKEAPI'].get_summary(pokemon_name)
        summary_translated = app.config['FUN_TRANSLATIONS'].translate_description(summary)
        return summary_translated

    @app.route('/pokemon/<pokemon_name>')
    def get_pokemon(pokemon_name) -> Response:
        summary = app.config['POKEAPI'].get_summary(pokemon_name)
        return summary

    return app


if __name__ == '__main__':
    create_app().run()
