from datastructures.queue.queue import Queue
from datastructures.stack.stack import Stack
from datastructures.LinkedList.singly import SinglyLinkedList

if __name__ == "__main__":
    # testing stack
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack)

    stack.pop()
    try:
        stack.pop()  # should raise EmptyStackException
    except Exception as e:
        print(e)

    # testing Queue
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    try:
        queue.dequeue()
    except Exception as e:
        print(e)

    print('\n\n***************** Testing Singly Linked List ***********************')
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(2)
    singly_linked_list.append(5)
    print(singly_linked_list)
    singly_linked_list.append(8)
    print(singly_linked_list)
