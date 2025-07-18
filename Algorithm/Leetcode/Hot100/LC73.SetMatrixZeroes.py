"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先记录下0出现的列，避免重复使用set
        zero_col: set[int] = set()
        for r in range(len(matrix)):
            has_zero: bool = False
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_col.add(c)
                    has_zero = True
            if has_zero:
                # 如果在当前发现过0，那么整行置0
                matrix[r][:] = [0] * len(matrix[0])
        for c in zero_col:
            for row in matrix:
                row[c] = 0
