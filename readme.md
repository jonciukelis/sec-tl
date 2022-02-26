# Software Engineering Challenge

Fancy Pokedex with translation capabilities.
- Endpoint ` /pokemon/<pokemon name> ` returns a pokedex entry for named pokemon.
- Endpoint ` /pokemon/translated/<pokemon name> ` returns a pokedex entry for named pokemon with the description translated into:
    - Shakespeare language
    - Yoda language (for cave types or legendary pokemon).

Both endpoints return:
```
{
    "name": str,
    "abilities": [str],
    "height": int,
    "weight": int,
    "types": [str],
    "base_happiness": int,
    "color": "str",
    "description": str,
    "habitat": str,
    "isLegendary": bool,
    "isMythical": bool
}
```

## Prerequisites

- Python 3
- Clone this repo
- Access to the internet

## Getting Started

- Create and activate a new virtual environment:
    ```
    $ python3 -m venv venv 
    $ . venv/bin/activate
    ```
- Install dependencies:
    - Either just for running
    ```
    $ pip install -e .
    ```
    - Or for development
    ```
    $ pip install -e .[test]
    ```
- Start the app:
    ```
    $ python app.py
    ```
- API endpoint available at http://localhost:5000