from typing import List

"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
解题思路：排序+异或法
1. 我们把数组进行排序，如果出现连续两个相等的数字，必然会出现以下情况 res == res ^ nums[i] ^ nums[i + 1]，其中 nums[i] == nums[i + 1]，
   那么我们就返回 nums[i] 即可；
2. 反之，如果一直没有满足以上条件出现，根据「鸽巢定理」，说明重复数字必然是第一个。
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        res: int = nums[0]
        for i in range(1, len(nums) - 1):
            if res == res ^ nums[i] ^ nums[i + 1]:
                return nums[i]
        return res
