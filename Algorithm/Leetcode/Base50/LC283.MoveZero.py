from typing import List


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""
class Solution:
    # 这是没经过优化的冒泡式移动，可以A题目，但是效率低
    # def bulbMoveZeroes(self, nums: List[int]) -> None:
    #     for i in range(1, len(nums)):
    #         j = i
    #         # 只要前面是0，就不断交换
    #         while j > 0 and nums[j - 1] == 0:
    #             nums[j], nums[j - 1] = nums[j - 1], nums[j]
    #             j -= 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        # j的作用是记录有多少个非0元素，j是非0元素的插入点
        # j是一个锚点，会自增，后面找到了非0元素就插入到j这个位置
        j: int = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        # j之前都是非0元素，之后就是全0咯
        for i in range(j, len(nums)):
            nums[i] = 0



if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
