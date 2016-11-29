from urllib import parse

import attr
import requests
from toolz import dicttoolz

import mtgsdk.utils as utils

ENDPOINT = 'sets'


@attr.s
class Set:
    border = attr.ib()
    code = attr.ib()
    name = attr.ib()
    release_date = attr.ib()
    type = attr.ib()

    block = utils.optional_attrib()
    booster = utils.optional_attrib()
    gatherer_code = utils.optional_attrib()
    magic_cards_info_code = utils.optional_attrib()
    mkm_id = utils.optional_attrib()
    mkm_name = utils.optional_attrib()
    old_code = utils.optional_attrib()
    online_only = utils.optional_attrib()


def from_code(code: str):
    url = parse.urljoin(utils.API_URL, ENDPOINT + '/' + code)
    resp = requests.get(url)
    resp.raise_for_status()
    return Set(**dicttoolz.keymap(utils.cc_to_us, resp.json()['set']))


def search(**kwargs):
    yield from utils.search(ENDPOINT, Set, **kwargs)
