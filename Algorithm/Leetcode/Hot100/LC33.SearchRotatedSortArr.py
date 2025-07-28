from typing import List

"""
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
解题思路：两次二分查找
1. 第一次二分查找的方法参考 LC153，根据 nums[-1] 来查找最小元素的下标，从而直到旋转了多少次；
2. 我们先将 nums 根据旋转的次数复原，然后进行第二次二分查找，从而得到复原之后的下标。最后通过取余操作返回旋转之后所在的下标位置。
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n: int = len(nums)
        min_idx: int = self.searchMinIdx(nums)
        nums[:] = nums[min_idx:] + nums[:min_idx]
        # 开区间写法
        l, r = -1, n
        while l + 1 < r:
            mid: int = (l + r) // 2
            if nums[mid] == target:
                return (mid + min_idx) % n
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        return -1

    def searchMinIdx(self, nums: List[int]) -> int:
        l, r = -1, len(nums) - 1
        while l + 1 < r:
            mid: int = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid
            else:
                r = mid
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
