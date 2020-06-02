from .node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, item) -> None:
        node = Node(item)
        if self.empty:
            self.root = node
            return

        current = self.root
        while current is not None:
            top = current
            if item > current.value:
                current = current.right
                if current is None:
                    top.right = node
            else:
                current = current.left
                if current is None:
                    top.left = node

    def find(self, item) -> bool:
        """
            must return boolean
        """
        current = self.root
        while current is not None:
            if item == current.value:
                return True
            elif item > current.value:
                current = current.right
            else:
                current = current.left
        return False



    @property
    def empty(self):
        return self.root is None

    def __repr__(self):
        return f'{self.root}'
