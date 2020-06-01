import pytest
from datastructures.LinkedList.doubly import DoublyLinkedList
from datastructures.LinkedList.exceptions import LinkedListEmptyError


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

    with pytest.raises(LinkedListEmptyError):
        doubly.insert_after(0, 10)

    doubly.append(1)
    doubly.append(2)
    doubly.append(3)

    doubly.insert_after(1, 10)
    assert doubly.items == [1, 10, 2, 3]

    doubly.insert_after(2, 20)
    assert doubly.items == [1, 10, 2, 20, 3]

    doubly.insert_after(3, 30)
    assert doubly.items == [1, 10, 2, 20, 3, 30]


def test_count():
    doubly = DoublyLinkedList()

    assert doubly.count == 0

    doubly.append(0)
    assert doubly.count == 1

