from .node import DoubleNode
from .exceptions import NodeNotExists


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

    def get_prev(self, item):
        next_node = self.get_node(item)
        return next_node.prev

    def insert_after(self, query, item):
        current = self.get_node(query)
        next_node = current.next

        if next_node is None:
            self.append(item)
        else:
            node = DoubleNode(item)
            self._insert_between(node, current, next_node)
            self._count += 1

    def insert_before(self, query, item):
        current = self.get_node(query)
        prev_node = current.prev
        if prev_node is None:
            self.prepend(item)
        else:
            node = DoubleNode(item)
            self._insert_between(node, prev_node, current)
            self._count += 1

    def delete(self, item):
        current = self.get_node(item)

        self._count -= 1
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

    def _insert_between(self, node, first_node, second_node):
        first_node.next, node.prev, second_node.prev, node.next = node, first_node, node, second_node

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
