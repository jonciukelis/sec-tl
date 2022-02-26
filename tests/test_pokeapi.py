import pytest
from pokeapi import _get_json_from_url
from requests import HTTPError
import requests_mock

def test__get_json_from_url(requests_mock):
    requests_mock.get('http://bad.status', status_code=500)
    with pytest.raises(HTTPError):
        _get_json_from_url("http://bad.status")