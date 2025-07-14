"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。
"""
from typing import List


class MyCircularQueue:

    def __init__(self, k: int):
        # 循环队列始终不需要删除元素。只需要移动head和tail，并且根据相对位置获取值即可
        self.size: int = k
        self.head: int = 0  # 指向队首，始终自增
        self.tail: int = 0  # 指向队尾，始终自增
        self.data: List[int] = [0] * k

    def getRelPos(self, abs_pos: int):
        return abs_pos % self.size

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.data[self.getRelPos(self.tail)] = value
            self.tail += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head += 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.getRelPos(self.head)]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.getRelPos(self.tail)]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return self.tail - self.head == self.size



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()