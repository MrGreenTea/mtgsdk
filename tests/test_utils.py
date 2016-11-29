from hypothesis import assume, given, strategies, note

from mtgsdk import utils


@given(strategies.text(min_size=1))
def test_camelcase_to_underscore(string):
    assume(all(c.lower().upper() == c or c.upper().lower() == c for c in string))
    # some characters change when they go through a upper/lower cycle. they can't be tested
    converted = utils.cc_to_us(string)
    assert converted == converted.lower()
    assert not converted.startswith('_')


@given(strategies.text(min_size=1), strategies.text(min_size=1))
def test_underscored_to_camelcase(string1, string2):
    assume('_' not in string1 and '_' not in string2)
    assume(all(not c.isalpha() or c.lower() != c or c.upper() != c for c in string1))
    assume(all(not c.isalpha() or c.lower() != c or c.upper() != c for c in string2))

    string = '_'.join((string1, string2))
    converted = utils.us_to_cc(string)
    note(converted)

    assert '_' not in converted
    assert any(c.isupper() or not c.isalpha() for c in converted)
    assert string1 in converted
    assert string2.capitalize() in converted
