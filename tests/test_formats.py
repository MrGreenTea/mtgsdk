from mtgsdki import formats


def test_formats():
    all_formats = list(formats.formats())
    assert len(all_formats) == 34
