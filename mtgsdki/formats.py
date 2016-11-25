from requests import get

def formats():
    resp = get('https://api.magicthegathering.io/v1/formats')
    resp.raise_for_status()
    yield from resp.json()['formats']
