from mtgsdki import sets


def test_all_sets():
    s = list(sets.search())
    assert len(s) == 200


def test_set():
    sets.from_code('KTK')
