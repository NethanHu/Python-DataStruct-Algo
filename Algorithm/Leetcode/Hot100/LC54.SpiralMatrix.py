import math
from typing import List

"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
解题思路：矩阵+硬编码
相比于上次提交（Base50）本方法优化了空间复杂度，虽然都是硬编码，但只使用x、y表示坐标，并且原地置math.inf表示已经遍历过，节省了空间。
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x, y, m, n = 0, 0, len(matrix), len(matrix[0])
        ans: List[int] = [matrix[0][0]]  # 只要先排除了第一个元素，之后的元素都满足下方的循环
        matrix[0][0] = '#'
        can_move: bool = True
        while can_move:
            can_move = False  # 如果下面所有的while都没有进入过，说明此时已经可以结束了
            while y < n - 1 and matrix[x][y + 1] != '#':
                y += 1
                ans.append(matrix[x][y])
                matrix[x][y] = '#'
                can_move = True

            while x < m - 1 and matrix[x + 1][y] != '#':
                x += 1
                ans.append(matrix[x][y])
                matrix[x][y] = '#'
                can_move = True

            while y > -1 and matrix[x][y - 1] != '#':
                y -= 1
                ans.append(matrix[x][y])
                matrix[x][y] = '#'
                can_move = True

            while x > -1 and matrix[x - 1][y] != '#':
                x -= 1
                ans.append(matrix[x][y])
                matrix[x][y] = '#'
                can_move = True

        return ans
