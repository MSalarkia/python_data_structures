from datastructures.queue.queue import Queue
from datastructures.stack.stack import Stack

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
        stack.pop() # should raise EmptyStackException 
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