"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
解题思路：手动哈希法
1. 我们先理一下思路，一个长度为N的nums数组，我们要找的那个缺失的正数只能是在[1, N + 1]之中：
    * 如果nums中有正有负有0，那么缺失的正数只会出现在[1, N]的某个地方；
    * 如果nums中全部都为正数，有大有小如[3, 1, 77, 4]，那么缺失的正数只会出现在[1, N]的某个slot中；
    * 如果nums中是有序的，比如[3, 1, 2, 4]，那么缺失的正数只有 5，也就是N + 1。
2. 我们不妨这样，我们最后要把数组改造成这样：
    * 下标为 i 的元素放 i + 1 的数字（可以不断把这个数字交换过来）；
    * 接着我们遍历的时候，如果发现下标为 i 的元素不为 i + 1，那么就返回 i + 1；否则就是len(nums) + 1。
3. 因为如果交换之后，对应下标 i 就能与 i + 1 数字的这个元素形成「一一对应」关系，如果没有对应上，说明就缺失了这个 i + 1 数字。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n: int = len(nums)
        for i in range(n):
            # 先判断这个数字有没有必要去哈希，如果类似于-1、77这种异常值，那我们保证了肯定有slot，那我们把精力放到有必要哈希的数字上
            # 再判断一下这个数字是不是放在了正确哈希位置上（下标的 i 的元素应该是数字 i + 1）
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 不可以用 nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # 因为 nums[nums[i] - 1] 是嵌套写法，求值可能会受到右边赋值的影响
                self.swap(nums, i, nums[i] - 1)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([3, 4, -1, 1]))
