from typing import List

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
解题思路：二分查找
1. 我们要记住这一套流程，这是很标准的双闭区间二分查找做法。
2. 实现细节：
    * 没有必要特判 nums[mid] = target 的情况，根据左指针的指向就可以知道target的具体位置，这也是鲁棒性的一种表现，因为如果元素不再数组中，会返回插入位置；
    * l、r 都为闭区间，循环调键位 l <= r，换句话说，如果 l 走过了 r 就会退出；
    * 第一个判断条件为 nums[mid] < target，可不能随意更改；且只有一个else。两者都将原来的指针变成 mid +/- 1；
    * 最后返回的是 left 指针。
3. 如果 target 就位于 l 指针的位置（target存在），那么 r 接下来会不断向 l 靠拢，直到走到 l 的左边，退出循环；
   如果 target 不存在，那么 l、r 最终重合在这个元素待插入的前一个元素位置，然后 l + 1 得到元素的具体插入位置，此时 l > r 退出循环。
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # l, r 都为闭区间
        l: int = 0
        r: int = len(nums) - 1
        while l <= r:
            mid: int = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 8, 9, 13, 16], 10))
