import requests

class FunTranslations():
    def __init__(self, uri):
        self.uri = uri

    def translate_description(self, summary):
        url = self.uri + _determine_translation_language(summary)
        summary['description'] = _retrieve_translated_text(url, summary['description'])
        return summary

def _determine_translation_language(summary):
    if summary['habitat'] == 'cave' or summary['isLegendary']:
        return 'yoda'
    return 'shakespeare'

def _retrieve_translated_text(url, text):
    data = {"text": text}
    
    resp = requests.post(url, json=data)

    if resp.status_code != requests.codes.ok:
        raise requests.HTTPError('FunTranslations API call to {} returned error {}'.format(url, resp.status_code))

    return resp.json()['contents']['translated']
