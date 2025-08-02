from typing import List, Counter

"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。
解题思路：快速排序（虽然灵神有更好的做法，但是本题适合自己手写一遍各种排序，就当复习）
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums)

    def inplace_swap(self, alist: List[int], i: int, j: int) -> None:
        alist[i], alist[j] = alist[j], alist[i]

    def partition(self, alist: List[int], first: int, last: int) -> int:
        pivot: int = alist[first]
        left: int = first + 1
        right: int = last

        done: bool = False
        while not done:
            while left <= right and alist[left] <= pivot:
                left += 1
            while left <= right and alist[right] >= pivot:
                right -= 1
            if left > right:
                done = True
            else:
                self.inplace_swap(alist, left, right)
        self.inplace_swap(alist, first, right)
        return right

    def quick_sort_helper(self, alist: List[int], first: int, last: int) -> None:
        if first < last:
            split: int = self.partition(alist, first, last)
            self.quick_sort_helper(alist, first, split - 1)
            self.quick_sort_helper(alist, split + 1, last)

    def quick_sort(self, alist: List[int]) -> None:
        self.quick_sort_helper(alist, 0, len(alist) - 1)

    # 或者我们知道只有 0、1、2 三个元素，用 Counter 统计各自的个数，然后依次把 nums 重新覆盖一遍，效率比快排更高。
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     color_cnt: dict[int, int] = Counter(nums)
    #     for i in range(color_cnt[0]):
    #         nums[i] = 0
    #     for i in range(color_cnt[0], color_cnt[0] + color_cnt[1]):
    #         nums[i] = 1
    #     for i in range(color_cnt[0] + color_cnt[1], len(nums)):
    #         nums[i] = 2
