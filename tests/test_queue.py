from datastructures.queue import Queue, QueueEmptyException
import pytest


def test_empty():
    queue = Queue()
    assert queue.empty is True


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.empty is False

    assert len(queue) == 3


def test_dequeue():
    queue = Queue()
    with pytest.raises(QueueEmptyException):
        queue.dequeue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    p = queue.dequeue()

    assert p == 1

    assert len(queue) == 2


def test_peek():
    queue = Queue()
    with pytest.raises(QueueEmptyException) as e:
        queue.peek()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.peek() == 1

    queue.dequeue()
    assert queue.peek() == 2

    queue.dequeue()
    assert queue.peek() == 3
