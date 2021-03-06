from datastructures.tree import BinarySearchTree
from datastructures.tree import Node


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


def test_is_valid():
    tree = initialize_tree()
    assert tree.is_valid is True

    tree2 = BinarySearchTree()
    n1 = Node(4)
    n2 = Node(6)
    n1.right = n2

    n3 = Node(5)
    n2.left = n3

    n4 = Node(2)
    n1.left = n4

    n5 = Node(8)
    n4.right = n5

    tree2.root = n1
    assert tree2.is_valid is False


def test_is_equal():
    tree1 = initialize_tree()
    tree2 = initialize_tree()

    assert tree1 == tree2

    tree2.root.right.left.value = 5
    assert tree1 != tree2


def test_kth_from_root():
    tree = initialize_tree()

    assert tree.kth_from_root(k=0) == [4]

    assert tree.kth_from_root(k=1) == [2, 7]

    assert tree.kth_from_root(k=2) == [1, 3, 6, 8]
