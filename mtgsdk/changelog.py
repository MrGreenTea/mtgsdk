import re
from typing import Iterator

import attr
from requests import get

__URL = 'https://raw.githubusercontent.com/MagicTheGathering/mtg-api/master/CHANGELOG.md'


@attr.s
class Version:
    details = attr.ib()
    release_date = attr.ib()
    version = attr.ib()


def full_changelog() -> Iterator[Version]:
    resp = get(__URL)
    resp.raise_for_status()
    pattern = re.compile(r'\([0-9]{4}-[0-9]{2}-[0-9]{2}\)')
    for _v in filter(None, resp.text.split('##')):  # filter empty splits (first one)
        match = pattern.search(_v)
        if match is None:
            continue
        version = _v[:match.start()].strip()
        release_date = _v[match.start()+1:match.end()-1]
        details = _v[match.end():].strip()
        yield Version(version=version, release_date=release_date, details=details)


def newest_version() -> Version:
    return next(full_changelog())


