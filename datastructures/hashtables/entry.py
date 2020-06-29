class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'Entry(key={self.key}, value={self.value})'


__all__ = ['Entry']
