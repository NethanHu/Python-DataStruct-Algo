"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
from typing import List


class Solution:
    # 下面的空间复杂度是O(n^2)，不是特别好
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n: int = len(matrix)
    #     # 变换很简单，row(1)变col(n-1)...row(n-1)变col(1)
    #     cols: List[List[int]] = [[] for _ in range(n)]
    #     for row in matrix:
    #         for i, n in enumerate(row):
    #             cols[i].append(n)
    #     for i, row in enumerate(matrix):
    #         row[:] = reversed(cols[i])

    class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            n: int = len(matrix)
            # 从数学上讲，顺时针旋转90度等于先转置再行反转，这样可以不用开辟别的空间
            # 我们直接遍历上三角矩阵，和下三角对称元素进行置换
            for r in range(n):
                for c in range(r, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            for row in matrix:
                row.reverse()