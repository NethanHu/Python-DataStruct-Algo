

"""
如果数组是单调递增或单调递减的，那么它是 单调 的。
如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i] >= nums[j]，那么数组 nums 是单调递减的。
当给定的数组 nums 是单调数组时返回 true，否则返回 false。
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 2:
            return True
        start: int = 1
        # 确保遍历完开头都是相同数字的情况，接下去才是开始
        while nums[start] - nums[start - 1] == 0:
            start += 1
        # 出现不相同的数字后，从下一对数字开始确定是升序还是降序
        order: int = 1 if nums[start] - nums[start - 1] > 0 else -1
        for i in range(start + 1, len(nums)):
            if (nums[i] - nums[i - 1]) * order < 0:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isMonotonic([1, 2, 2, 3]))