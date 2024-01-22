import pytest

from utils.dicts import get_val


@pytest.mark.parametrize('collection, key, expected', [
    ({2: 3, 4: 5}, 10, 'git'),
    ({2: 3, 4: 5}, 2, 3),
    ({'some': 'thing'}, 'some', 'thing'),
    ({}, "", 'git')
])
def test_dicts(collection, key, expected):
    assert get_val(collection, key) == expected
