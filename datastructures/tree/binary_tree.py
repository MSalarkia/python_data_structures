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
    def depth(self):
        def calculate_depth(node):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return 1

            return 1 + max(calculate_depth(node.right), calculate_depth(node.left))
        return calculate_depth(self.root)

    @property
    def maximum(self):
        maximum = self.root.value if self.root else None
        current = self.root.right

        while current is not None:
            if current.value > maximum:
                maximum = current.value
            current = current.right

        return maximum

    @property
    def breadth_first_items(self):
        output = []
        current = self.root
        to_be_traversed = [current]

        def traverse(node):
            if node is None:
                return

            while len(to_be_traversed) != 0:
                node = to_be_traversed.pop()
                output.append(node.value)

                if node.left is not None:
                    to_be_traversed.insert(0, node.left)
                if node.right is not None:
                    to_be_traversed.insert(0, node.right)

        traverse(current)
        return output

    @property
    def items(self):
        output = []
        current = self.root

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            output.append(node.value)
            traverse(node.right)

        traverse(current)
        return output

    @property
    def empty(self):
        return self.root is None

    def __repr__(self):
        return f'{self.root}'
