from .node import SingleNode


class NodeNotExists(Exception):
    pass


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

    def prepend(self, item):
        node = SingleNode(item)

        if self.empty:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_after(self, item, new_value):
        current = self.head
        node = SingleNode(new_value)

        while current is not None:
            if current.value == item:
                node.next = current.next
                current.next = node
                break
            current = current.next
        else:
            raise NodeNotExists(f'node with value={item} does not exist!')

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
