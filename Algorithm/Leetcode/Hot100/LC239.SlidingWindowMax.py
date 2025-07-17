from collections import deque
from typing import List, Deque

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
解题思路：单调队列+滑动窗口
1. zip函数很好的控制了i、j两个指针的初始化和循环次数问题，让i从0之前起手，j从第0位起手；i<0的时候什么事都不用做，只要看j表演就行。
2. 当queue中没有元素，就直接append；如果有元素，我们分类讨论：
    * 且如果j位置的那个数字小于等于queue中的最后一位，因为至少在窗口期内是非严格递减的，我们加入它；
    * 如果j位置那个数字大于queue中最后一位，我们就把循环着queue中末尾的元素踢掉，直到有位置换上更有潜力的新数字。
3. 当i开始进入>=0之后，对于i我们有几项事情需要做：
    * 如果i指针已经到当前queue中最大值（第0位置上的那个）之后了，那说明窗口已经扫完了最大值，就要把queue中king位置的元素popleft走了，
      取而代之的是queue中最有潜力的老二位置；
    * 因为queue中最大值就在第0位，所以每次扫完之后都要记录下0位元素，这就是该窗口的最大值。
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans: List[int] = []
        n: int = len(nums)
        queue: Deque[int] = deque()
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 如果在nums数组中i指针遍历过了当前最大值，从左边pop出去
            if i > 0 and queue[0] == nums[i - 1]:
                queue.popleft()
            # 在添加新元素的时候，如果发现queue最后一个元素比要加入的元素小
            # 那么最后一个元素必然不可能会成为下一个最大值，直接pop出去。我们循环这一个过程，直到新元素不再大于queue中最后一位
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            # 每次移动一次，我们记录下最大值，而最大值就在queue的第一位
            if i >= 0:
                ans.append(queue[0])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
