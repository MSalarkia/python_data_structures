from ..stack.stack import Stack

class QueueEmptyException(Exception):
    pass

class Queue:
    '''
    this class implements a queue with 2 stacks
    '''
    def __init__(self):
        self._enqueue_stack = Stack()
        self._dequeue_stack = Stack()
        
    def enqueue(self, item):
        self._enqueue_stack.push(item)
        
    def dequeue(self):
        if self.empty():
            raise QueueEmptyException('Queue is empty.')
        
        self.exchange_data_between_stacks()
                
        return self._dequeue_stack.pop()
    
    def empty(self):
        return self._enqueue_stack.empty() and self._dequeue_stack.empty()
    
    def exchange_data_between_stacks(self):
        if self._dequeue_stack.empty():
            while not self._enqueue_stack.empty():
                self._dequeue_stack.push(self._enqueue_stack.pop())
    
    def peek(self):
        self.exchange_data_between_stacks()
        
        return self._dequeue_stack.peek()

