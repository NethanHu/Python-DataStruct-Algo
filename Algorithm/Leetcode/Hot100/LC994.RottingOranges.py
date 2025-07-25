from collections import deque
from typing import List, Deque

"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
解题思路：BFS
1. 我们观察腐烂橘子的「感染进度」，每一分钟就感染自己身边一圈，我们可以类比是层层变化的，因此我们自然而然会想到BFS的做法：
    * BFS会每次把腐烂橘子的坐标放到一个队列中，当队列不为空的时候，就每次popleft出腐烂橘子的位置；
    * 如果身边有新鲜橘子，就将其「感染」，数字设置成为2；依次循环往复，知道queue中不再有元素；
    * 注意每次进入一层的时候都需要将ans+1.
2. 如果最后还是会有新鲜橘子，我们就返回为-1；否则返回ans。
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 这里 -1 是为了凑一个提前量。因为min0的时候是popleft出初始烂橘子的位置，所以我们凑一个-1在前面。
        ans: int = -1
        queue: Deque[tuple[int, int]] = deque()
        # 初始化queue，指的是在0分钟的时候腐烂的橘子的位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '2':
                    queue.append((i, j))

        # 这里加一个条件约束，如果grid全是0，一个烂橘子/新鲜橘子都没有，那就返回0
        if not queue and not any(1 in r for r in grid):
            return 0

        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                # 四个方向「感染」一次
                if i > 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    queue.append((i - 1, j))
                if i < m - 1 and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    queue.append((i + 1, j))
                if j > 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    queue.append((i, j - 1))
                if j < n - 1 and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    queue.append((i, j + 1))

        # 最后检查一下还有没有新鲜的橘子存在
        for row in grid:
            if 1 in row:
                return -1

        return ans
