from typing import List

"""
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 
就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。必须 原地 修改，只允许使用额外常数空间。
解题思路：从个别推导到一般的技巧
1. 这里不展开分析角度，可以参考该视频：https://www.bilibili.com/video/BV1bvKrzwEDK/?share_source=copy_web&vd_source=4462f9f91cf69d0596e719cbf56bea30；
2. 我们主要分析解题的细节，我们可以推导出有以下几个步骤：
    * 首先是从右向左，找第一个小于右侧相邻数字的数下标 target；注意，此时如果发现遍历到第 0 位仍没有的时候，说明整个数组已经是最大的字典顺序了，直接原地逆序；
    * 然后找到 target 右边第一个不小于 nums[target] 的元素；注意我们用的是 >= 符号，因为如果出现 [1, 5, 1, 0] 这样数组时，我们让第一个 1 交换的元素应该是 5，所以应该在出现 == 的时候也需要停下：
      交换的逻辑其实是让 target 和停下之前的元素做交换：nums[target], nums[i - 1] = nums[i - 1], nums[target]；
    * 最后我们以 target 为界，左边都是不需要排列的，让 nums[target + 1:] 的元素做一个逆序的调整，这里使用 reversed 函数进行迭代，如上方交换之后的 [5, 1, 1, 0] 变成 [5, 0, 1, 1]。
      能直接逆序交换的原因是：我们确保了 target 右边元素是「单调性」的。
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            nums.reverse()
            return

        target: int = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[target]:
                target = i
                break
            else:
                target = i
                if i == 0:
                    # 说明所有元素完全逆序，就直接reverse
                    nums.reverse()
                    return

        # 如果 target 在中间找到，我们开始顺序遍历；找到右边第一个不小于 nums[target] 的元素
        # 此时可以取到相等的含义是：假设数组是 [1, 5, 1]，我们 target 为 0，我们要让 1, 5 交换的必要条件就是在遍历到 i = 2 的时候进入原地交换的步骤
        for i in range(target + 1, len(nums)):
            if nums[target] >= nums[i]:
                # 此时 i - 1 就是第一个比 target 更大的元素，我们要进行交换
                nums[target], nums[i - 1] = nums[i - 1], nums[target]
                break
            if i == len(nums) - 1:
                nums[target], nums[i] = nums[i], nums[target]

        for i, e in enumerate(reversed(nums[target + 1:])):
            nums[target + 1 + i] = e


if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1, 5, 1]))
