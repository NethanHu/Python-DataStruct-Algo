from typing import List

"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""


class Solution:
    # 整体思路是排序+双指针，难点在于去重
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []

        size: int = len(nums)
        nums.sort()
        ans: List[List[int]] = []

        for i in range(size - 2):
            # 这是对于锚点数的去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 如果当前数字已经大于0，那么三数之和不可能为0
            if nums[i] > 0:
                break
            # 左右双指针来查找合适的三元组
            l: int = i + 1
            r: int = size - 1
            while l < r:
                cur_sum: int = nums[i] + nums[l] + nums[r]
                if cur_sum > 0:
                    # 只要大于0，我们就左移动右指针，不需要关心是否有多个连续相等的数字
                    r -= 1
                if cur_sum < 0:
                    # 只要小于0，我们就右移动左指针，不需要关心是否有多个连续相等的数字
                    l += 1
                if cur_sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    # 找到一组相等的数字之后，我们要去重，一直增加指针直到新的数字
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    # 因为左边的数字改变，和右边数字之和肯定不为0，因此要移动就移动两边
                    l += 1
                    r -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
