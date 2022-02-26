import pytest
from pokeapi import _get_json_from_url
from requests import HTTPError
import requests_mock  # noqa: F401


def test__get_json_from_url(requests_mock):  # noqa: F811
    requests_mock.get('http://bad.status', status_code=500)
    with pytest.raises(HTTPError):
        _get_json_from_url("http://bad.status")
