"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
解题思路：前缀和（优化：可以不开辟数组）
1. 这里只需要我们求最大和的连续子数组，按照定义，就是前缀和数组中 max(后面的一个大值减去前面的一个小值)
2. 我们在遍历的时候，动态的更新当前发现的最小值min_pre_sum
3. 由于记忆性，更新max_sum的时候必然是需要晚于min_pre_sum的，因此我们把cur_sum - min_pre_sum作为当前的候选值
4. max_sum是全局的，但是min_pre_sum、cur_sum这两个是动态变化的，时间前后如下：
    * 我们首先获取到了cur_sum，我们先算算这个位置能不能和前面的min_pre_sum做差得到更大的max_sum；
    * 接着更新min_pre_sum；
    * 一路循环到nums结束。
"""
import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_pre_sum: int = 0
        max_sum = -math.inf
        cur_sum: int = 0
        for n in nums:
            cur_sum += n
            max_sum = max(max_sum, cur_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, cur_sum)
        return max_sum
