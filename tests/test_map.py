from datastructures.hashtables.map import Map
import pytest


def test_get():
    map = Map()
    map.add('name', 'John')
    map.add(1, 'one')

    with pytest.raises(KeyError):
        map.get(2)

    assert map.get('name') == 'John'
    assert map.get(1) == 'one'


def test_add():
    map = Map()
    name = 'John'
    map.add('name', name)
    assert map.get('name') == name

    name2 = 'David'
    map.add('name', name2)
    assert map.get('name') == name2

    map.add(1, 'one')
    map.add(6, 'six')

    assert map.get(1) == 'one'

    assert map.get(6) == 'six'


def test_delete():
    map = Map()
    map.add('name', 'John')

    map.add(1, 'one')
    map.add(2, 'two')
    map.add(3, 'three')
    map.add(4, 'four')
    map.add(5, 'five')

    with pytest.raises(KeyError):
        map.delete(10)

    with pytest.raises(KeyError):
        map.delete('family')

    map.delete(1)

    with pytest.raises(KeyError):
        map.get(1)

