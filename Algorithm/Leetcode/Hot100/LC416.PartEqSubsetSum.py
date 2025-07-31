from typing import List

"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
解题思路：动态规划

1. 首先，我们可以将原问题进行转化。题目要求判断数组是否能被分割成两个和相等的子集。
   设数组所有元素的总和为 total_sum。如果 total_sum 是奇数，那么不可能分割成两个和相等的整数子集，直接返回 False。
   如果 total_sum 是偶数，那么每个子集的和都必须是 target = total_sum / 2。此时，问题就转化为了：能否从 nums 数组中挑选出若干个元素，使得它们的和恰好等于 target？
   这正是抽象的01背包问题，对于当前需要填的数字，我们凑出来的数不能超过它（不能超越重量），但是又必须达到特定价值（价值就是这个数字本身）。
2. DP 数组的定义为：dp[j] 表示，在使用 nums 中的部分或全部数字时，对于一个容量为 j 的背包，我们能凑出的最大价值（即最大子集和）：
    * 我们的目标就是检查 dp[target] 的最终值。如果 dp[target] == target，说明我们成功地用 nums 中的数字凑出了 target，即背包被恰好装满。
3. 关于「选不选」当前数字，我们可以采用一个常规思路去解决这个问题，即：
    * 我们的 max 函数的含义是：在「选了该数字后，不超过减去当前数字的剩余大小」的情况下，「求和后最贴近该剩余数」的某个子集的总和；
    * 对于我们期待的总和 target，我们设置一个 DP 数组，初始化 dp[0] = 0，很好理解，因为我们在要求为 0 的时候什么也没法选；
    * 我们采用递推公式，在选择了当前数字下标 i 之后，从 target 开始，我们用 j 遍历剩余大小 [0, nums[i]]（这也是 j - nums[i] 的定义域）：
      对于当前填入的数字 j，我们 dp[j] 的选择是，我们要么找到第 j - nums[i] 个元素（此时肯定 <= j - nums[i]），加上当前选中的 nums[i]，求得
      在「选中第 i 个数字的时候」，对于 j 这个总和要求，我们能从数组中拼凑出的「最大逼近 j 的值」。
3. 举个例子，在当前数组 [1, 5, 11, 5] 的情况下，它的总和是偶数，因此可以尝试找到两个相等子集。它的总和一半为11，因此我们尝试寻找其中和为11的子集。
   在遍历完之后，dp 数组为：
            这里dp[11]=11的含义是，我们想找和为11的子集，最终可以凑出来（因此可以提前返回 True）
                                       ↓
   [0, 1, 1, 1, 1, 5, 6, 6, 6, 6, 10, 11]
                         ↑
    这里dp[7]=6的含义是，我们想找和为7的子集，但是最终只能凑出 6
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target: int = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        dp: List[int] = [0] * (target + 1)
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                # 归根到底 [nums[i], target] 不重要，重要的是 j - nums[i] 的定义域
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
            if dp[target] == target:
                return True
        return target == dp[target]


if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))
