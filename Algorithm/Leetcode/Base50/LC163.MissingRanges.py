
"""
给你一个闭区间 [lower, upper] 和一个 按从小到大排序 的整数数组 nums ，其中元素的范围在闭区间 [lower, upper] 当中。

如果一个数字 x 在 [lower, upper] 区间内，并且 x 不在 nums 中，则认为 x 缺失。

返回 准确涵盖所有缺失数字 的 最小排序 区间列表。也就是说，nums 的任何元素都不在任何区间内，并且每个缺失的数字都在其中一个区间内。
"""
from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        if lower == upper and lower in nums:
            return []
        ans: List[List[int]] = []
        # 我们设置一个当前最小值当成lower bound
        cur_lower: int = lower
        for n in nums:
            # 如果当前最小值在nums当中，把当前最小值+1然后继续
            if cur_lower == n:
                cur_lower += 1
            # 如果nums中的n比当前最小值更大，也没有超过最大值
            # 就把lower bound和n-1当成一个答案append进ans
            elif cur_lower < n <= upper:
                ans.append([cur_lower, n - 1])
                cur_lower = n + 1
            else:
                # 如果n比upper更大，就退出循环
                break
        # 遍历完所有的n之后，如果还未达到upper bound，就手动加入最后一个range
        if upper >= cur_lower:
            ans.append([cur_lower, upper])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
    print(s.findMissingRanges([-1], -2, -1))
    print(s.findMissingRanges([-1], -1, 0))