from typing import List

"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
解题思路：贪心算法
1. 我们只需要一次遍历即可，我们维护两个变量：「当前最小的价格」和「最大收益」
2. 我们从头开始遍历 prices，每当遍历到当前 p，我们会有两个分支：
    * 如果当前 p 比历史上的 min_p 要小，那么必然当前 p - min_p 是个负数，此时肯定还是原来的 max_inc 更大（尽管可能是0），不可能更新 max_inc，不过在这个节点我们可以把 min_p 变成当前 p；
    * 否则，我们计算当前 p 和 min_p 之间的差值，如果比之前最大收入更大，那么就将 max_inc 更新为 p - min_p（我们在这里使用的是 max 函数）。
3. 本题就是一道简单贪心算法，一次遍历即可，不需要维护 DP。
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_inc = 0
        for p in prices:
            if p < min_p:
                min_p = p
            else:
                max_inc = max(max_inc, p - min_p)
        return max_inc
