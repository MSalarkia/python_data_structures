from datastructures.queue.queue import Queue
from datastructures.stack.stack import Stack
from datastructures.LinkedList.singly import SinglyLinkedList
from datastructures.LinkedList.doubly import DoublyLinkedList
from datastructures.hashtables.map import Map
from datastructures.tree.binary_tree import BinarySearchTree

if __name__ == "__main__":
    # You can test algorithms and data structures here
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(1)
    tree.insert(9)
    tree.insert(7)

    print(tree)

    print(2, tree.find(2))
    print(3, tree.find(3))
    print(7, tree.find(7))
    print(14, tree.find(14))
    print(6, tree.find(6))
