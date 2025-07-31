from typing import List

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。问总共有多少条不同的路径？
解题思路：二维动态规划
1. 递推的公式为：当前格子的路径数 paths[r][c] = 上方个格子往下走一格 paths[r - 1][c] + 左边的格子向右走一格 paths[r][c - 1]
2. 初始化条件为全部设置成 1，这样是为了让第一行和第一列都为 1，因为走完第一行或第一列有且只有一条路径可选。
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        paths: List[List[int]] = [[1 for _ in range(n)] for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                paths[r][c] = paths[r - 1][c] + paths[r][c - 1]
        return paths[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3, 7))
