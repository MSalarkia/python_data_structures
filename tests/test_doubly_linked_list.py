import pytest
from datastructures.linkedlist import DoublyLinkedList
from datastructures.linkedlist import NodeNotExists


def test_append():
    doubly = DoublyLinkedList()
    assert doubly.items == []

    doubly.append(0)

    assert doubly.items == [0]

    doubly.append(1)
    assert doubly.items == [0, 1]

    assert doubly.count == 2


def test_prepend():
    doubly = DoublyLinkedList()

    doubly.prepend(0)
    assert doubly.items == [0]

    doubly.prepend(1)
    assert doubly.items == [1, 0]

    assert doubly.count == 2


def test_insert_after():
    doubly = DoublyLinkedList()

    doubly.append(1)
    doubly.append(2)
    doubly.append(3)

    doubly.insert_after(1, 10)
    assert doubly.items == [1, 10, 2, 3]
    assert doubly.count == 4

    doubly.insert_after(2, 20)
    assert doubly.items == [1, 10, 2, 20, 3]
    assert doubly.count == 5

    doubly.insert_after(3, 30)
    assert doubly.items == [1, 10, 2, 20, 3, 30]
    assert doubly.count == 6


def test_count():
    doubly = DoublyLinkedList()

    assert doubly.count == 0

    doubly.append(0)
    assert doubly.count == 1


def test_delete():
    doubly = DoublyLinkedList()

    with pytest.raises(NodeNotExists):
        doubly.delete(1)

    doubly.append(1)
    doubly.append(2)
    doubly.append(3)
    doubly.append(4)

    assert doubly.count == 4

    doubly.delete(2)
    assert doubly.items == [1, 3, 4]
    assert doubly.count == 3

    doubly.delete(1)
    assert doubly.items == [3, 4]

    doubly.delete(4)
    assert doubly.items == [3]

    doubly.delete(3)
    assert doubly.items == []
    assert doubly.count == 0


def test_insert_before():
    doubly = DoublyLinkedList()
    with pytest.raises(NodeNotExists):
        doubly.insert_before(1, 0)

    doubly.append(1)
    doubly.append(2)
    doubly.append(3)

    doubly.insert_before(1, 10)
    assert doubly.items == [10, 1, 2, 3]

    doubly.insert_before(2, 20)
    assert doubly.items == [10, 1, 20, 2, 3]

    doubly.insert_before(3, 30)
    assert doubly.items == [10, 1, 20, 2, 30, 3]

    assert doubly.count == 6
