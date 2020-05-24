print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

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
        if self.empty():
            raise EmptyStackException('Stack is empty.')
        return self._items.pop()
    
    def empty(self):
        return len(self) == 0
    
    def peek(self):
        if self.empty():
            raise EmptyStackException('Stack is empty.')
            
        return self._items[-1]
        
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return str(self._items)


if __name__ == '__main__':
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack)

    print(stack.pop())

    print(stack.pop())
    print(stack)

    stack.pop()
    stack.pop() # should raise EmptyStackException 