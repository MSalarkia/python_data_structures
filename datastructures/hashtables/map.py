from .entry import Entry

__all__ = ['Map']


class Map:
    def __init__(self):
        self.size = 5
        self.list = [[] for i in range(self.size)]

    def _hash(self, key):
        return abs(hash(key)) % self.size

    def add(self, key, value):
        _, bucket = self._find_bucket(key)
        new_entry = Entry(key, value)

        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return

        bucket.append(new_entry)

    def get(self, key):
        _, bucket = self._find_bucket(key)
        for entry in bucket:
            if entry.key == key:
                return entry.value

        raise KeyError(f'key {key} does not exist.')

    def delete(self, key):
        index, bucket = self._find_bucket(key)
        original_bucket_size = len(bucket)
        filtered_bucket = [entry for entry in bucket if entry.key != key]
        filtered_bucket_size = len(filtered_bucket)

        if original_bucket_size == filtered_bucket_size:
            raise KeyError(f'key {key} does not exist')

        self.list[index] = filtered_bucket

    def _find_bucket(self, key):
        index = self._hash(key)
        bucket = self.list[index]
        return index, bucket

    def __repr__(self):
        output = ''
        for bucket in self.list:
            for entry in bucket:
                output += f'{entry.key}={entry.value}, '
        return f'Map({output[:-2]})'
