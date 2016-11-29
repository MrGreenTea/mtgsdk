from mtgsdk import types


def test_types():
    all_types = list(types.types())
    assert len(all_types) == 13


def test_supertypes():
    all_supertypes = list(types.supertypes())
    assert len(all_supertypes) == 5


def test_subtypes():
    all_subtypes = list(types.subtypes())
    assert len(all_subtypes) == 341
