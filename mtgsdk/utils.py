import itertools
from functools import partial
from urllib import parse

import attr
import requests
from toolz import dicttoolz

API_URL = 'https://api.magicthegathering.io/v1/'


optional_attrib = partial(attr.ib, default=None, hash=False, repr=False, cmp=False)
no_repr_attrib = partial(attr.ib, repr=False)
no_hash_attrib = partial(attr.ib, hash=False)
no_cmp_attrib = partial(attr.ib, hash=False, cmp=False)


def us_to_cc(string: str) -> str:
    """Convert camelCase string to underscore separated string."""
    split_input = string.split('_')
    return split_input[0] + ''.join(s.capitalize() for s in split_input[1:])


def cc_to_us(string: str) -> str:
    """Convert underscore separated string to underscore separated string camelCase string."""
    s = ''.join('_' + c.lower() if c.isupper() else c for c in string)
    if s[0:1] == '_':
        s = s[1:]
    return s


def build_query(endpoint, **kwargs):
    kwargs = dicttoolz.keymap(us_to_cc, kwargs)
    # translate parameters from image_url into camelCase for magicthegatheringio
    query = parse.urljoin(API_URL, endpoint) + '?' + parse.urlencode(kwargs)
    return query


def object_from_dict(cls, dictionary=None):
    def _inner(dict_) -> cls:
        return cls(**dicttoolz.keymap(cc_to_us, dict_))
    if dictionary is None:
        return _inner

    return _inner(dictionary)


def search(endpoint, cls, **kwargs):
    def _get_page(page):
        query = build_query(endpoint, page=page, **kwargs)
        response = requests.get(query)
        response.raise_for_status()

        response = response.json()[endpoint]
        if not response:
            raise IndexError

        yield from map(object_from_dict(cls), response)

    if 'page' in kwargs:
        try:
            yield from _get_page(kwargs.pop('page'))
        except IndexError:
            return
    else:
        for page_num in itertools.count(1):
            try:
                yield from _get_page(page_num)
            except IndexError:
                break
