from collections import deque

class Deque:
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def add_front(self, item):
        self._items.appendleft(item)

    def add_rear(self, item):
        self._items.append(item)

    def pop_front(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def pop_rear(self):
        if self.is_empty():
            return None
        return self._items.pop()

