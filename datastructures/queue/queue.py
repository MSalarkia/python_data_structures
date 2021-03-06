from ..stack.stack import Stack

__all__ = ['QueueEmptyException', 'Queue']


class QueueEmptyException(Exception):
    pass


class Queue:
    """
    this class implements a queue with 2 stacks
    """

    def __init__(self):
        self._enqueue_stack = Stack()
        self._dequeue_stack = Stack()
        self._count = 0

    def enqueue(self, item):
        self._enqueue_stack.push(item)
        self._count += 1

    def dequeue(self):
        if self.empty:
            raise QueueEmptyException('Queue is empty.')

        self.exchange_data_between_stacks()
        self._count -= 1
        return self._dequeue_stack.pop()

    @property
    def empty(self):
        return self._enqueue_stack.empty and self._dequeue_stack.empty

    def __len__(self):
        return self._count

    def exchange_data_between_stacks(self):
        if self._dequeue_stack.empty:
            while not self._enqueue_stack.empty:
                self._dequeue_stack.push(self._enqueue_stack.pop())

    def peek(self):
        if self.empty:
            raise QueueEmptyException('Queue is empty.')

        self.exchange_data_between_stacks()

        return self._dequeue_stack.peek()
