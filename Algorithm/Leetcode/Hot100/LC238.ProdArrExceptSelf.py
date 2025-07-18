"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
解题思路：记忆化+前缀积+后缀积。核心在于一点：如果知道了 i 「左边」所有数的乘积，以及 i 「右边」所有数的乘积，就可以算出 answer[i]
1. 我们先回忆一下前缀和/积的定义，指的是没有「当前元素」的情况下，当前元素前面的所有元素的和/积
2. 初始化条件是1，因为1乘任何数都为其自身，从第一个元素开始乘上1就开始了我们的遍历。那么[]数组的积为1，前缀积第一个元素为1，后缀积同理
3. 我们同时构造前缀积和后缀积
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        # 同时构造第 i 个元素的前后缀，answer[i] = pre[i] * suf[i]
        pre: List[int] = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        suf: List[int] = [1] * n
        for j in range(n - 2, -1, -1):
            suf[j] = suf[j + 1] * nums[j + 1]
        return [p * s for p, s in zip(pre, suf)]
