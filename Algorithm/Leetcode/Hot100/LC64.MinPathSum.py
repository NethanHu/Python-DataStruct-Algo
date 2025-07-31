from typing import List

"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步
解题思路：二维动态规划
1. 我们设置一个二维 DP 数组 path_sum，为了方便动态规划，我们初始化的时候直接让它 copy 一份 grid；
2. 由于只能向下和向右，因此第一行从左向右只能不断累加，第一列从上到下只能不断累加，所以真正的递推是从 [1, 1] 开始（这也是为什么我们要对 m, n 为 1 的时候进行额外判断）
    * 递推公式为：当前格子路径最小值 path_sum[r][c] =「上面格子的最优值 path_sum[r - 1][c] + 当前格子」和「左边格子的最优值 path_sum[r][c - 1] + 当前格子」两者更小的。
3. 最后输出 path_sum[-1][-1] 即可。
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1:
            return sum(grid[0])
        if n == 1:
            return sum([grid[r][0] for r in range(m)])
        # 初始化工作
        path_sum: List[List[int]] = [[0 for _ in range(n)] for _ in range(m)]
        path_sum[0][0] = grid[0][0]
        for c in range(1, n):
            path_sum[0][c] += grid[0][c - 1]
        for r in range(1, m):
            path_sum[r][0] += grid[r - 1][0]
        # 开始填表
        for r in range(1, m):
            for c in range(1, n):
                path_sum[r][c] = min(grid[r][c] + path_sum[r - 1][c], grid[r][c] + path_sum[r][c - 1])
        return path_sum[-1][-1]
