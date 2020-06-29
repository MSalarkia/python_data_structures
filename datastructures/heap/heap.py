import math

__all__ = ['Heap']


class Heap:
    """
    using list as the underlying data structure for building a Heap
    """

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

        self.bubble_up(target_index=len(self) - 1)

    def bubble_up(self, target_index):
        if target_index == 0:
            return

        parent_index = self.calc_parent_index(target_index + 1)

        last_item = self.items[target_index]

        if self.items[parent_index] < last_item:
            self.items[parent_index], self.items[target_index] = self.items[target_index], self.items[parent_index]
            self.bubble_up(parent_index)

    def remove_top(self):
        self.items[0] = -math.inf
        self.items = self.items[1:]
        if self.items[0] < self.items[1]:
            self.items[0], self.items[1] = self.items[1], self.items[0]

        for target_index in range(len(self) - 1, 1, -1):
            self.bubble_up(target_index=target_index)

    def calc_parent_index(self, child_index):
        return math.floor(child_index / 2) - 1

    def calc_level(self, level):
        return math.ceil(math.log(level, 2))

    @property
    def max(self):
        return self.items[0]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f'{self.items}'
