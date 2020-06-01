from datastructures.queue.queue import Queue
from datastructures.stack.stack import Stack
from datastructures.LinkedList.singly import SinglyLinkedList
from datastructures.LinkedList.doubly import DoublyLinkedList
from datastructures.hashtables.map import Map

if __name__ == "__main__":
    # You can test algorithms and data structures here
    doubly = DoublyLinkedList()
    doubly.append(1)
    doubly.append(2)
    doubly.append(3)
    print(doubly)

    doubly.insert_after(1, 10)
    print(doubly)

    doubly.delete(10)
    print('after delete 10', doubly)

    doubly.delete(3)
    print('after delete 3', doubly)

    doubly.delete(1)
    print('after delete 1', doubly)

    # doubly.delete(1)
    # print(doubly)
    #
    # doubly.delete(1)
    # print(doubly)

    # doubly.delete(1)
    # print(doubly)


