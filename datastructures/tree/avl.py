from .node import AVLNode


class AVLTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, node, item):
        if node is None:
            return AVLNode(item)
        if item > node.value:
            node.right = self._insert_recursive(node.right, item)

        if item < node.value:
            node.left = self._insert_recursive(node.left, item)

        node.height = self.height(node)
        return node

    def insert(self, item):
        self.root = self._insert_recursive(self.root, item)

    def height(self, n):
        def calculate_height(node):
            if node is None:
                return -1

            if node.left is None and node.right is None:
                return 0

            return 1 + max(calculate_height(node.right), calculate_height(node.left))

        return calculate_height(n)

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
