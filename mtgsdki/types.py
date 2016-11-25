from requests import get


def types():
    resp = get('https://api.magicthegathering.io/v1/types')
    resp.raise_for_status()
    yield from resp.json()['types']


def supertypes():
    resp = get('https://api.magicthegathering.io/v1/supertypes')
    resp.raise_for_status()
    yield from resp.json()['supertypes']


def subtypes():
    resp = get('https://api.magicthegathering.io/v1/subtypes')
    resp.raise_for_status()
    yield from resp.json()['subtypes']
