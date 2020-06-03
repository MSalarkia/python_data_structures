from .node import Node
import math


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

    def kth_from_root(self, k):
        output = []

        def extract_nodes(node, level):
            if node is None:
                return
            if level == k:
                return output.append(node.value)

            extract_nodes(node.left, level + 1)
            extract_nodes(node.right, level + 1)

        extract_nodes(self.root, 0)
        return output

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

    def __eq__(self, other):
        if not isinstance(other, BinarySearchTree):
            return False

        def is_sub_tree_equal(self_node, other_node):
            if self_node is None and other_node is None:
                return True

            if self_node is None or other_node is None:
                return False

            return self_node.value == other_node.value and \
                   is_sub_tree_equal(self_node.left, other_node.left) and \
                   is_sub_tree_equal(self_node.right, other_node.right)

        return is_sub_tree_equal(self.root, other.root)

    def __ne__(self, other):
        return not (self == other)

    @property
    def is_valid(self):
        def calc_is_valid(node, min_range, max_range):
            if node is None:
                return True

            if min_range <= node.value <= max_range:
                left_min = min_range
                left_max = node.value
                right_min = node.value
                right_max = max_range
                return calc_is_valid(node.left, left_min, left_max) and calc_is_valid(node.right, right_min, right_max)

            return False

        current = self.root
        return calc_is_valid(current, -math.inf, math.inf)

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
    def minimum(self):
        minimum = self.root.value if self.root else None
        current = self.root.left

        while current is not None:
            if current.value < minimum:
                minimum = current.value
            current = current.left

        return minimum

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
