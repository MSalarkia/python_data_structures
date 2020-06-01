from .node import DoubleNode
from .exceptions import NodeNotExists, LinkedListEmptyError


# TODO: Deleting Node Test
# TODO: insert_before
# TODO: Inserrt before test
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def append(self, item):
        node = DoubleNode(item)
        if self.empty:
            self.head = self.tail = node
            self._count = 1
            return

        self._count += 1

        tail = self.tail
        node.prev = tail
        tail.next = node
        self.tail = node
        # node.prev, self.tail, self.tail.next = self.tail, node, node

    def prepend(self, item):
        node = DoubleNode(item)
        if self.empty:
            self.head = self.tail = node
            self._count = 1
            return

        head = self.head
        head.prev = node
        node.next = head
        self.head = node
        self._count += 1

    def get_node(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return current
            current = current.next

        raise NodeNotExists(f'node with value {item} does not exist.')

    def insert_after(self, query, item):
        if self.empty:
            raise LinkedListEmptyError('DoublyLinkedList is empty.')
        node = DoubleNode(item)
        current = self.get_node(query)

        next_node = current.next
        node.next = next_node
        node.prev = current
        current.next = node
        if next_node is not None:
            next_node.prev = node
        self._count += 1

    def delete(self, item):
        current = self.get_node(item)

        next_node = current.next
        prev_node = current.prev

        if prev_node is None and next_node is None:
            self.head = None
            self.tail = None
            return

        if next_node is None:
            prev_node.next = None
            self.tail = prev_node
        else:
            next_node.prev = prev_node

        if prev_node is None:
            next_node.prev = None
            self.head = next_node
        else:
            prev_node.next = next_node
        self._count -= 1

    @property
    def count(self):
        return self._count

    @property
    def empty(self):
        return self._count == 0

    @property
    def items(self):
        output = []
        current = self.head
        while current is not None:
            output.append(current.value)
            current = current.next
        return output

    def __repr__(self):
        return f'DoublyLinkedList(items={self.items})'
