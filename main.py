from datastructures.queue.queue import Queue
from datastructures.stack.stack import Stack
from datastructures.linkedlist.singly import SinglyLinkedList
from datastructures.linkedlist.doubly import DoublyLinkedList
from datastructures.hashtables.map import Map
from datastructures.tree.binary_tree import BinarySearchTree
from datastructures.tree.avl import AVLTree
from datastructures.heap.heap import Heap
from datastructures.tree.node import Node

if __name__ == "__main__":
    # You can test algorithms and data structures here
    # tree = BinarySearchTree()
    # tree.insert(3)
    # tree.insert(5)
    # tree.insert(2)
    # tree.insert(3)
    # tree.insert(4)
    # tree.insert(1)
    # tree.insert(9)
    # tree.insert(12)
    # tree.insert(7)
    # tree.insert(6)
    # tree.insert(6.5)
    # tree.insert(5.5)
    # tree.insert(2.5)
    # tree.insert(2.75)
    #
    #
    # print(tree)
    #
    # print(2, tree.find(2))
    # print(3, tree.find(3))
    # print(7, tree.find(7))
    # print(14, tree.find(14))
    # print(6, tree.find(6))
    #
    # print(tree.items)
    #
    # print(tree.breadth_first_items)
    #
    # print('max', tree.maximum)
    # print('min', tree.minimum)
    #
    # print(tree.depth)
    #
    # print('is valid', tree.is_valid)
    #
    # print('kth from root', tree.kth_from_root(6))
    #
    # print('height', tree.height(tree.root.left.right))
    #
    # #
    # # avl = AVLTree()
    # # avl.insert(45)
    # # avl.insert(12)
    # # avl.insert(35)
    # # avl.insert(14)
    # # avl.insert(80)
    # # avl.insert(74)
    # # print(avl)
    # # print('unbalanced', avl.unbalanced)
    #
    # avl = AVLTree()
    # avl.insert(10)
    # avl.insert(20)
    # avl.insert(30)
    # avl.insert(5)
    # avl.insert(15)
    # avl.insert(0)
    # avl.insert(40)
    # avl.insert(25)
    # avl.insert(2)
    # avl.insert(7)
    # avl.insert(12)
    # avl.insert(18)
    # avl.insert(22)
    # avl.insert(27)
    # avl.insert(35)
    # avl.insert(45)
    # # avl.insert(50)
    # # print('unbalanced', avl.unbalanced)
    # print(avl)
    heap = Heap()
    heap.insert(10)
    heap.insert(5)
    heap.insert(6)
    heap.insert(20)
    heap.insert(3)
    heap.insert(9)
    heap.insert(7)
    heap.insert(4)
    heap.insert(40)
    heap.insert(25)
    print(heap)

    heap.remove_top()
    print(heap)