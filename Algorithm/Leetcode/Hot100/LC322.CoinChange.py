from typing import List

"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
解题思路：记忆化搜索
1. 我们创建一个DP数组来获取递推中的记忆信息。初始化 DP[0] = 0，即在 amount 为 0 的时候，一个硬币都不需要。
2. 递推关系为，我们遍历所有的金额 i，由于有多枚硬币，我们记忆化搜索在使用这一枚硬币之后，剩下的金额从 DP 数组中去搜索：
    * 我们设置一个硬币数量集合 coin_combs，把「使用完当前 coin 之后，剩余金额里面总的最优数量」放进去； 
    * 如果当前 coin 已经大于金额，那么我们不再进行搜索，跳过（否则 i - coin 就为负数，数组越界）；
    * 如果 dp[i - coin] 搜索到的结果是 -1，即在使用当前 coin 之后剩下的金额无解，所以我们跳过该 coin，继续寻找下一个 coin；
    * 在寻找完所有的 coin 之后，我们从 coin_combs 获取最小值（即最优的兑换数量）；如果 coin_combs 为空，说明一个有效的组合都没有，那么当前 i 就是 -1。
3. 本题是进阶版的 LC279 题，相对而言由于金额有限制（比如不再会有数值为 1 的硬币，对应着平方数中去除了 1），那么会增加一些 -1 的结果和相关的条件判断。
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: List[int] = [10000] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            coin_combs: List[int] = []
            for coin in coins:
                if coin <= i:
                    # 如果当前 [i - 其中一枚 coin] 的记忆化搜索中不为 -1，才进行以下操作
                    if dp[i - coin] != -1:
                        cur_comb: int = dp[i - coin] + 1
                        coin_combs.append(cur_comb)
            dp[i] = min(coin_combs) if coin_combs else -1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
