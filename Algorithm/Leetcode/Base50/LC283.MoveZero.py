from typing import List


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            j = i
            # 只要前面是0，就不断交换
            while j > 0 and nums[j - 1] == 0:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
