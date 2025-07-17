"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。
解题思路：前缀和+两数之和
1. “前缀和”定义：如果从索引 i 到 j 的子数组之和为 k，那么必然有 sum(nums[i...j]) = k
2. 而 sum(nums[i...j]) 等于 sum(nums[0...j]) - sum(nums[0...i-1])。
   如果我们用 pre[x] 表示从 0 到 x 的前缀和，那么上面的公式就是：pre[j] - pre[i-1] = k
3. 变换一下，就得到：pre[i-1] = pre[j] - k
"""
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count: int = 0
        # 前缀和
        pre: int = 0
        pre_map: dict[int, int] = defaultdict(int)
        # 这一步很重要，相当于初始化pre_map。在遍历开始之前，我们已经有 1 种方法可以得到和为 0 的前缀和（就是什么都不选，子数组是[]）
        # 因为如果我们出现了pre-k==0的情况时，我们可以选择[]+nums[:i+1]的这种做法
        pre_map[0] = 1
        for i in range(len(nums)):
            pre += nums[i]
            # 如果不初始化，这里就会少进入一次
            if pre - k in pre_map.keys():
                count += pre_map.get(pre - k)
            pre_map[pre] += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))