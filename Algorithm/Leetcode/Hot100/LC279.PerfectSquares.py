from math import isqrt
from typing import List

"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
解题思路：记忆化搜索
1. 我们直接使用DP从头开始填表，并且在后面使用记忆化搜索的方式；我们先来解决一下DP的几个步骤：
    * 初始化条件，n = 0 的时候，意思是此时的最优解是选0个元素；
    * 状态转移方程：当前数字是 i，那么平方数可以选的是 1, ..., j（j 为 i 开方之后向下取整），我们遍历 j，在取完 j 之后还剩下 i - j * j，
      此时我们从记忆化的DP数组中去查询，当当前数字是 i - j * j 的时候，最优的取法是取几个数字；
    * 那么状态转移方程就是 dp[i] = min(dp[i], dp[i - j * j] + 1)，我们要 dp[i] 继续比较的原因是，我们还要继续遍历 j，指不定遍历到什么时候反而取得元素更多，我们还是选择保持自身。
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # 采用填表式的递推
        dp: List[int] = [10000] * (n + 1)
        # dp[0] == 0，毋庸置疑，这表示还剩0的时候，最优可以选0个元素
        dp[0] = 0
        for i in range(1, n + 1):
            upper: int = isqrt(i)
            for j in range(upper, 0, -1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                # 简单优化，如果遍历到就是平方数，那么直接跳过，因此此时最优解就是只取一个数
                if i == j * j:
                    break
        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(7207))
