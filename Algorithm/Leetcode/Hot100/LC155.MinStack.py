from typing import List

"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
解题思路：二元栈
1. 我们使用 Python 原生 List 来当做栈使用，因为我们只用到 pop 功能；
2. 难点在于如何在 pop 完一个元素之后，我们能够动态地调整栈中的最小值信息：
    * 我们使用一个二元元组来保存当前值和历史上的最小值，那么在 pop 的时候就能够「回溯」到曾经的一个状态；
    * 那个时候的状态被保留下来，我们可以从 self.stack[-1][1] 马上读到此时的最小值是多少。
"""


class MinStack:

    def __init__(self):
        # stack 同时维护当前的val和历史最小值
        self.stack: List[tuple[int, int]] = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            prev_min: int = self.stack[-1][1]
            if val < prev_min:
                self.stack.append((val, val))
            else:
                self.stack.append((val, prev_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
