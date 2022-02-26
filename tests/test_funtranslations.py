import pytest
from funtranslations import _determine_translation_language, _retrieve_translated_text
from requests import HTTPError
import requests_mock

def test__determine_translation_language():
    assert _determine_translation_language({'habitat': 'cave', 'isLegendary': False}) == 'yoda'
    assert _determine_translation_language({'habitat': 'urban','isLegendary': True}) == 'yoda'
    assert _determine_translation_language({'habitat': 'urban','isLegendary': False}) == 'shakespeare'

def test__retrieve_translated_text(requests_mock):
    requests_mock.post('http://bad.status', status_code=500)
    with pytest.raises(HTTPError):
        _retrieve_translated_text("http://bad.status","")