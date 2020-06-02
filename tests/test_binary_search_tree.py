import pytest
from datastructures.tree.binary_tree import BinarySearchTree


def initialize_tree():
    tree = BinarySearchTree()
    #           4
    #         /   \
    #        2     7
    #       / \   / \
    #      1  3  6   8
    tree.insert(4)
    tree.insert(7)
    tree.insert(2)
    tree.insert(8)
    tree.insert(6)
    tree.insert(3)
    tree.insert(1)
    return tree


def test_insert():
    tree = initialize_tree()

    assert tree.items == [1, 2, 3, 4, 6, 7, 8]


def test_find():
    tree = initialize_tree()

    assert tree.find(1) is True

    assert tree.find(4) is True

    assert tree.find(5) is False


def test_breadth_first_search():
    tree = initialize_tree()

    assert tree.breadth_first_items == [4, 2, 7, 1, 3, 6, 8]


def test_depth():
    tree = initialize_tree()
    assert tree.depth == 3

    tree.insert(10)
    assert tree.depth == 4
