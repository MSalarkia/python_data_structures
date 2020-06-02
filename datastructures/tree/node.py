class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def __repr__(self):
        return f'Node(value={self.value}, right={self.right}, left={self.left})'
