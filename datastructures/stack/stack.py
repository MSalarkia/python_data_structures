class EmptyStackException(Exception):
    pass


class Stack:
    '''
    this class implements stacks using a python list which is not ideals
    '''

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.empty:
            raise EmptyStackException('Stack is empty.')
        return self._items.pop()

    def peek(self):
        if self.empty:
            raise EmptyStackException('Stack is empty.')

        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return str(self._items)

    @property
    def empty(self):
        return len(self) == 0
