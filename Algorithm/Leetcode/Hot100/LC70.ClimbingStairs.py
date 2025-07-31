"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
解题思路：动态规划
1. 我们找到状态转移方程：f(next) = f(cur) + f(pre)，即走到 next 这一个格子的时候，可以由 cur 一步走到，或者 pre 两步走到；
2. 我们设置提前退出条件，n == 1 和 n == 2 两个时候，接下来就直接递归推出答案即可。
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 我们找到状态转移方程 f(i + 1) = f(i) + f(i - 1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        s_pre: int = 1
        s_cur: int = 2
        for _ in range(n - 2):
            s_nxt: int = s_pre + s_cur
            s_pre = s_cur
            s_cur = s_nxt
        return s_nxt
