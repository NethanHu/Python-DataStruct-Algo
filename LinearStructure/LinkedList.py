from abc import ABC, abstractmethod

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(ABC):
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def remove(self, item) -> bool:
        current = self.head
        prev = None
        found = False
        # 先进行查找对应item的位置
        while current is not None and not found:
            if current.get_data() == item:
                found = True  # if found, then skip the while-loop
            else:
                prev = current
                current = current.get_next()

        if found:
            # Case 1. 如果发现的节点的首节点
            if prev is None:
                # 即让首节点变成该节点的下一个即可
                self.head = current.get_next()
            else: # Case 2. 如果节点在中间
                # 即让prev的下一个节点变成current的下一个节点，跳过current
                prev.set_next(current.get_next())
            return True

        else:
            print(f"Cannot find item {item} in the list.")
            return False

    @abstractmethod
    def search(self, item) -> bool:
        pass

    @abstractmethod
    def add(self, item):
        pass



class UnorderedList(LinkedList):
    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def search(self, item) -> bool:
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False


class OrderedList(LinkedList):
    def add(self, item):
        current = self.head
        prev = None
        new_node = Node(item)

        # 查找插入位置，算法确保插入的位置在相同值的第一位
        while current is not None and current.get_data() < item:
            prev = current
            current = current.get_next()

        # 如果插入位置是在链表的第一位
        if prev is None:
            new_node.set_next(self.head)
            self.head = new_node
        else: # 插入的位置在链表中间
            new_node.set_next(current)
            prev.set_next(new_node)


    def search(self, item) -> bool:
        current = self.head
        while current is not None:
            if current.get_data() == item:
                return True
            elif current.get_data() > item:
                return False
            current = current.get_next()
        return False

