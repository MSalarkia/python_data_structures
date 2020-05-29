from .node import SingleNode


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, item):
        node = SingleNode(item)

        if self.empty:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    @property
    def empty(self):
        return self.tail is None and self.head is None

    @property
    def items(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values
    
    def __repr__(self):
        return f'SinglyLinkedList(values={str([x for x in self.items])})'