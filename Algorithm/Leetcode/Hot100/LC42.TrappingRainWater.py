from collections import deque
from typing import List, Deque

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
解题思路：单调栈+横向求解
1. 遍历高度数组。
2. 当栈为空，或者当前柱子高度 h 小于等于栈顶柱子的高度时，直接将当前柱子的 (索引, 高度) 入栈。这维持了栈的单调递减特性。
3. 当当前柱子高度 h 大于栈顶柱子的高度时，我们找到了一个可以积水的“凹槽”。
    a. 记录并弹出栈顶元素，这个是凹槽的“底部” (mid_idx, mid_h)。
    b. 如果此时栈不为空，那么新的栈顶元素就是凹槽的“左墙” (left_idx, left_h)。
    c. 当前的柱子 (i, h) 就是凹槽的“右墙”。
    d. 计算积水：
        * 水的高度 = min(左墙高度, 右墙高度) - 凹槽底部高度
        * 水的宽度 = 右墙索引 - 左墙索引 - 1
        * 将计算出的面积累加到总和。
    e. 继续这个出栈、计算的过程，直到栈为空或者新的栈顶比当前柱子 h 更高。
4. 完成上述 while 循环后，将当前这个“右墙”柱子 (i, h) 压入栈中。
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        area: int = 0
        # 我们为了直观，在单调栈中保存下标i和高度h的二元组
        stack: Deque[int] = deque()
        for i, h in enumerate(height):
            # 当单调栈有元素，碰到了当前高度导致不单调递减的时候
            while stack and h > height[stack[-1]]:
                # 把当前bottom的下标pop出来
                mid_i = stack.pop()
                # 如果stack此时为空，说明没有左边界了，就直接退出这个while-loop
                if not stack:
                    break
                left_i: int = stack[-1]
                right_i: int = i
                # 计算横向雨水面积，沿着一定的高度，找到动态的width计算面积
                area += self.getArea(height[mid_i], height[left_i], h, right_i - left_i - 1)
            # 结束完这一部分的雨水面积计算（或者没计算）之后，不要忘了把当前的元素添加到单调栈
            stack.append(i)
        return area

    def getArea(self, cur_h: int, left_h: int, right_h: int, width: int) -> int:
        min_h: int = min(left_h, right_h) - cur_h
        return min_h * width