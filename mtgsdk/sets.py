from urllib import parse
from typing import Iterator

import attr
import requests
from toolz import dicttoolz

import mtgsdk.utils as utils

ENDPOINT = 'sets'


@attr.s
class Set:
    border = utils.no_repr_attrib()
    code = attr.ib()
    name = attr.ib()
    release_date = utils.no_repr_attrib()
    type = utils.no_repr_attrib()

    block = utils.optional_attrib()
    booster = utils.optional_attrib()
    gatherer_code = utils.optional_attrib()
    magic_cards_info_code = utils.optional_attrib()
    mkm_id = utils.optional_attrib()
    mkm_name = utils.optional_attrib()
    old_code = utils.optional_attrib()
    online_only = utils.optional_attrib()


def from_code(code: str) -> Set:
    url = parse.urljoin(utils.API_URL, ENDPOINT + '/' + code)
    resp = requests.get(url)
    resp.raise_for_status()
    return utils.object_from_dict(Set, resp.json()['set'])


def search(**kwargs) -> Iterator[Set]:
    return utils.search(ENDPOINT, Set, **kwargs)
