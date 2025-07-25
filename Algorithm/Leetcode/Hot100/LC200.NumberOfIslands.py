from typing import List

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
解题思路：DFS
1. 如果我们找到了一块陆地，我们要从这个点出发，把一整个陆地「感染」，这样我们就得到了陆地与陆地之间“连通图”的关系；
2. 我们设计一个DFS函数，首先要排除特殊情况，即该点无法向上/下/左/右走的时候，同样也不能走向海洋/已「感染」的陆地；
    * 那么经过一整个深度优先搜索之后，进无可进的时候就是整个联通的陆地被完全走完，并且被我们打上了已经遍历过的标记。
3. 每次找到一个尚未发现的陆地，就从这个点出发把整个岛占领，并将答案+1。
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> None:
            if (i < 0 or i >= m) or (j < 0 or j >= n) or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            dfs(i, j - 1)  # 往左走
            dfs(i, j + 1)  # 往右走
            dfs(i - 1, j)  # 往上走
            dfs(i + 1, j)  # 往下走

        ans: int = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans
