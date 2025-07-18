import math
from typing import List

"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
解题思路：矩阵+硬编码
相比于上次提交（Base50）本方法优化了空间复杂度，虽然都是硬编码，但只使用x、y表示坐标，并且原地置math.inf表示已经遍历过，节省了空间。
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h: int = len(matrix)
        w: int = len(matrix[0])
        ans: List[int] = []
        x, y = 0, 0  # x是行坐标，y是列坐标
        while True:
            stop: bool = True
            # 往右边走，直到碰到边界或者是无穷就停下换方向
            while y <= w:
                if y == w or matrix[x][y] == math.inf:
                    y -= 1
                    x += 1
                    break
                stop = False
                ans.append(matrix[x][y])
                matrix[x][y] = math.inf
                y += 1
            # 往下边走，直到碰到边界或者是无穷就停下换方向
            while x <= h:
                if x == h or matrix[x][y] == math.inf:
                    x -= 1
                    y -= 1
                    break
                stop = False
                ans.append(matrix[x][y])
                matrix[x][y] = math.inf
                x += 1
            # 往左边走，直到碰到边界或者是无穷就停下换方向
            while y <= w:
                if y == -1 or matrix[x][y] == math.inf:
                    y += 1
                    x -= 1
                    break
                stop = False
                ans.append(matrix[x][y])
                matrix[x][y] = math.inf
                y -= 1
            # 往上边走，直到碰到边界或者是无穷就停下换方向
            while x <= h:
                if x == -1 or matrix[x][y] == math.inf:
                    x += 1
                    y += 1
                    break
                stop = False
                ans.append(matrix[x][y])
                matrix[x][y] = math.inf
                x -= 1
            if stop:
                break
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
