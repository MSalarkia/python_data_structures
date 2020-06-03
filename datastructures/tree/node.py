class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def __repr__(self):
        return f'Node(value={self.value}, right={self.right}, left={self.left})'


class AVLNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.height = 0
        self.value = value

    def __repr__(self):
        return f'Node(value={self.value}, height={self.height}, right={self.right}, left={self.left})'
