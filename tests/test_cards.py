import requests
from hypothesis import assume, given, strategies

from mtgsdk import cards


@given(page=strategies.integers(min_value=1, max_value=321))
def test_first_page(page):
    c = list(cards.search(page=page))
    assert len(c) <= 100


@given(card_id=strategies.integers(min_value=1))
def test_from_id(card_id):
    try:
        cards.from_id(card_id)
    except requests.HTTPError:
        pass


@given(name=strategies.text())
def test_exact_search(name):
    assume('|' not in name and '%' not in name)
    results = list(cards.search(name=repr(name)))
    assert len(results) <= 1


@given(name=strategies.text(strategies.characters(
    blacklist_categories=('Cc', 'Cf', 'Cn', 'Co', 'Cs'), blacklist_characters='%')))
def test_search(name):
    assume(name != '|')
    list(cards.search(name=name, page=1))
