import attr
from requests import get

from mtgsdk import utils

__URL = 'https://api.magicthegathering.io/v1/changelogs'


@attr.s
class Version:
    details = attr.ib()
    id = attr.ib()
    release_date = attr.ib()
    version = attr.ib()


def full_changelog():
    resp = get(__URL)
    resp.raise_for_status()
    return map(utils.object_from_dict(Version), resp.json()['changelogs'])


def newest_version():
    resp = get(__URL + '?pageSize=1')
    resp.raise_for_status()
    return Version(**resp.json()['changelog'][0])

