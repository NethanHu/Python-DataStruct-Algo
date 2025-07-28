from typing import List

"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
解题思路：二分查找
1. 我们使用闭区间的方式来写这个问题，相对于上一题 LC74，闭区间的循环不变量是 [l, r]，那么循环的条件就是 l <= r，因为 l == r 的时候是一个合理的答案区间；
    * 原本的闭区间写法，如果发现一个 nums[mid] == target 就直接返回。但是我们这里要做的是找到一连串相等数字里面的第一个，换句话说：
    * 我们的 findLowerBound 函数「不在意」右边界有没有找到，有边界的作用只是不断去缩短 mid 的范围；
    * 这个方法就不是返回要找的元素的下标，因为 nums[mid] == target 的时候不返回，只是把 r 再往左移。如果 r 把自己从 target 元素的第一位往左移一位了，
      说明接下来只有 l 不断右移直到 l == r + 1 然后循环退出，此时 l 位于「第一个」target 元素的最左边；
2. 这个方法如何复用呢？
    * 我们先让它找到 target 第一次出现的位置，如果 target 比所有元素都要大，就会出现 start == len(nums)，也就是「插入」位置；
    * 如果 target 不存在，返回的只是「插入」位置，就会出现 nums[start] != target；
    * 如果 target 存在，那必然返回的就是第一次出现 target 的位置（r 从第一个元素身上左移之后的右移一位版本）。
3. 我们在找到第一次出现的 start 位置了之后，我们要找到 target 出现的最后一个位置。由于我们没有实现这个方法（如果想要实现也可以，把 findLowerBound 符号改一下）， 
    * 我们换个思路，找到第一个大于 target 的数字下标，然后往前找一位就是 target 最后一次出现位置；
    * 我们直接使用这个方法 findLowerBound(nums, target + 1) - 1，如果有 target + 1 元素，那就是返回第一次出现的位置；如果没有，那就是第一个在 target 后「插入」的数字。
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start: int = self.findLowerBound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end: int = self.findLowerBound(nums, target + 1) - 1
        return [start, end]

    def findLowerBound(self, nums: List[int], target: int) -> int:
        # 闭区间写法
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # 这个判断条件是精髓，因为我们找的是最小的左边界
            # 如果我们发现 nums[mid] == target，我们忽略它，继续往左找
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
