from utils.dicts import get_val


def test_dicts():
    assert get_val({2: 3, 4: 5}, 10) == 'git'
    assert get_val({'some': 'thing'}, 'some') == 'thing'
    assert get_val({}, "") == 'git'
