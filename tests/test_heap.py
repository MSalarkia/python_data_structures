from datastructures.heap.heap import Heap


def test_insert():
    heap = Heap()
    heap.insert(1)
    assert heap.items == [1]

    heap.insert(2)
    assert heap.items == [2, 1]

    heap.insert(3)
    assert heap.items == [3, 1, 2]