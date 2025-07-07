from _collections import deque

class Stack:
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return not self._items

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __iter__(self):  # 从栈顶到栈底（最后进入的元素第一个遍历）
        return reversed(self._items)

    def __str__(self) -> str:
        return f"Stack(Bottom -> {list(self._items)} <- Top)"