from urllib import parse

import attr
import requests
import toolz

import mtgsdk.utils as utils

ENDPOINT = 'cards'


@attr.s()
class Card:
    """represents a Card"""
    artist = utils.no_repr_attrib()
    id = utils.no_repr_attrib()
    layout = utils.no_repr_attrib()
    name = attr.ib()
    printings = utils.no_repr_attrib()
    rarity = utils.no_repr_attrib()
    set = attr.ib()
    set_name = utils.no_repr_attrib()
    type = utils.no_repr_attrib()

    cmc = utils.no_repr_attrib(default=0)
    colors = utils.no_repr_attrib(default=attr.Factory(list))
    color_identity = utils.no_repr_attrib(default=attr.Factory(list))
    image_url = utils.no_repr_attrib(default=None)
    flavor = utils.no_repr_attrib(default='')
    foreign_names = utils.no_repr_attrib(default=attr.Factory(list))
    legalities = utils.no_repr_attrib(default=attr.Factory(list))
    mana_cost = utils.no_repr_attrib(default=None)
    multiverseid = utils.no_repr_attrib(default=None)
    names = utils.no_repr_attrib(default=attr.Factory(list))
    power = utils.no_repr_attrib(default=None)
    rulings = utils.no_repr_attrib(default=attr.Factory(list))
    release_date = utils.no_repr_attrib(default=None)
    reserved = utils.no_repr_attrib(default=False)
    source = utils.no_repr_attrib(default=None)
    starter = utils.no_repr_attrib(default=False)
    subtypes = utils.no_repr_attrib(default=attr.Factory(list))
    supertypes = utils.no_repr_attrib(default=attr.Factory(list))
    text = utils.no_repr_attrib(default='')
    timeshifted = utils.no_repr_attrib(default=False)
    types = utils.no_repr_attrib(default=attr.Factory(list))
    toughness = utils.no_repr_attrib(default=None)
    variations = utils.no_repr_attrib(default=attr.Factory(list))

    border = utils.optional_attrib()
    hand = utils.optional_attrib()
    life = utils.optional_attrib()
    loyalty = utils.optional_attrib()
    number = utils.optional_attrib()
    original_text = utils.optional_attrib()
    original_type = utils.optional_attrib()
    watermark = utils.optional_attrib()


def from_id(card_id):
    url = parse.urljoin(utils.API_URL, ENDPOINT + '/' + str(card_id))
    resp = requests.get(url)
    resp.raise_for_status()
    return Card(**toolz.keymap(utils.cc_to_us, resp.json()['card']))


def search(**kwargs):
    # translate parameters from image_url into camelCase for magicthegatheringio
    yield from utils.search(ENDPOINT, Card, **kwargs)
