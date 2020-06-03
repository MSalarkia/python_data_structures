from .node import AVLNode


class AVLTree:
    def __init__(self):
        self.root = None
        self.unbalanced = False

    def _insert_recursive(self, node, item):
        if node is None:
            return AVLNode(item)

        if item > node.value:
            node.right = self._insert_recursive(node.right, item)

        if item < node.value:
            node.left = self._insert_recursive(node.left, item)

        self.reset_height(node)

        return self.balance(node)

    def reset_height(self, node):
        node.height = self.height(node)

    def balance(self, node):
        lr_difference = self.balance_factor(node)
        if lr_difference > 1:
            self.unbalanced = True
            left_node_balance_factor = self.balance_factor(node.left)
            if left_node_balance_factor < 0:
                node.left = self._rotate_left(node.left)

            return self._rotate_right(node)

        if lr_difference < -1:
            self.unbalanced = True
            right_node_balance_factor = self.balance_factor(node.right)
            if right_node_balance_factor > 0:
                node.right = self._rotate_right(node.right)

            return self._rotate_left(node)

        return node

    def _rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.reset_height(node)
        self.reset_height(new_root)
        return new_root

    def _rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.reset_height(node)
        self.reset_height(new_root)
        return new_root

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def insert(self, item):
        self.unbalanced = False
        self.root = self._insert_recursive(self.root, item)

    def _calculate_height(self, node):
        if node is None:
            return -1

        if node.left is None and node.right is None:
            return 0

        return 1 + max(self._calculate_height(node.right), self._calculate_height(node.left))

    def height(self, n):
        return self._calculate_height(n)

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

    def __repr__(self):
        return f'{self.root}'
