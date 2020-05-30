from .node import SingleNode


class NodeNotExists(Exception):
    pass


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, item):
        node = SingleNode(item)

        if self.empty:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1

    def prepend(self, item):
        node = SingleNode(item)

        if self.empty:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def insert_after(self, item, new_value):
        node = SingleNode(new_value)
        current = self._find_node(item)
        node.next = current.next
        current.next = node
        self.count += 1

    def _find_prev(self, item):
        prev, current = None, self.head
        while current is not None:
            if current.value == item:
                return prev

            prev, current = current, current.next

        raise NodeNotExists(f'node with value={item} does not exist!')

    def _find_node(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return current
            current = current.next

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

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    def __repr__(self):
        return f'SinglyLinkedList(values={str([x for x in self.items])})'
