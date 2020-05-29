class SingleNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        if isinstance(node, SingleNode) or node is None:
            self._next = node
        else:
            raise ValueError('node must be a SingleNode object')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    # Making it more beautiful
    def __repr__(self):
        return f'SingleNode(value={self.value}'
