from collections import deque
from typing import List, Deque

"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
解题思路：使用神奇工具Deque
Deque的pop、append复杂度都是O(1)，那么轮转数组的复杂度就可以降到O(k)。最后赋值的时候应该采用如下形式：
    nums[:] = list(rotating)
这样才能把新的值赋到nums内存地址中。
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k 可能大于数组长度，需要取模
        k = k % len(nums)
        if k == 0:
            return
        rotating: Deque[int] = deque(nums)
        for _ in range(k):
            rotating.appendleft(rotating.pop())
        nums[:] = list(rotating)
