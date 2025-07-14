from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def __str__(self) -> str:
        return f"Queue(front -> {list(self._items)} <- rear)"