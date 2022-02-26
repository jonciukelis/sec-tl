from flask import Flask, json, Response

def create_app() -> Flask:
    """Create a configured Flash app instance."""
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/pokemon/translated/<pokemon_name>')
    def get_pokemon_translated(pokemon_name) -> Response:
        return {'get_pokemon_translated': 'called'}

    @app.route('/pokemon/<pokemon_name>')
    def get_pokemon(pokemon_name) -> Response:
        return {'get_pokemon': 'called'}
        
    return app


if __name__ == '__main__':
    create_app().run()
