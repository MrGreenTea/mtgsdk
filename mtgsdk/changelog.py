from requests import get

__URL = 'https://api.magicthegathering.io/v1/changelogs'


def full_changelog():
    resp = get(__URL)
    resp.raise_for_status()
    return resp.json()['changelogs']


def newest_version():
    return full_changelog()[0]


