from datastructures.LinkedList.singly import SinglyLinkedList
from datastructures.LinkedList.exceptions import NodeNotExists
import pytest


def test_count():
    singly_linked_list = SinglyLinkedList()
    assert singly_linked_list.count == 0

    singly_linked_list.append(1)
    assert singly_linked_list.count == 1

    singly_linked_list.prepend(2)
    assert singly_linked_list.count == 2

    singly_linked_list.insert_after(2, 3)
    assert singly_linked_list.count == 3

    singly_linked_list.delete(2)
    assert singly_linked_list.count == 2


def test_append():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    assert singly_linked_list.items == [1, 2, 3]


def test_prepend():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.prepend(1)
    assert singly_linked_list.count == 1

    singly_linked_list.prepend(2)
    assert singly_linked_list.items == [2, 1]


def test_delete():
    singly_linked_list = SinglyLinkedList()
    with pytest.raises(NodeNotExists):
        singly_linked_list.delete(1)

    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.prepend(3)
    singly_linked_list.delete(2)
    assert singly_linked_list.items == [3, 1]
    singly_linked_list.delete(1)
    assert singly_linked_list.items == [3]
    singly_linked_list.delete(3)
    assert singly_linked_list.items == []


def test_insert_after():
    singly_linked_list = SinglyLinkedList()
    with pytest.raises(NodeNotExists):
        singly_linked_list.insert_after(1, 10)

    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.insert_after(1, 10)
    assert singly_linked_list.items == [1, 10, 2, 3]

    singly_linked_list.insert_after(2, 20)
    assert singly_linked_list.items == [1, 10, 2, 20, 3]

    singly_linked_list.insert_after(3, 30)
    assert singly_linked_list.items == [1, 10, 2, 20, 3, 30]
