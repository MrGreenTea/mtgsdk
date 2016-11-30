from mtgsdk import changelog


def test_newest_version():
    newest_version = changelog.newest_version()
    assert all(int(i) >= 0 for i in newest_version.version.split('.'))


def test_full_changelog():
    full_changelog = list(changelog.full_changelog())
    for change in full_changelog:
        assert all(int(i) >= 0 for i in change.version.split('.'))
