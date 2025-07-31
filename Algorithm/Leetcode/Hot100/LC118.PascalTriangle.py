from typing import List

"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        ans: List[List[int]] = [[1], [1, 1]]
        for i in range(2, numRows):
            cur_row: List[int] = [1]
            for j in range(len(ans[i - 1]) - 1):
                cur_row.append(ans[i - 1][j] + ans[i - 1][j + 1])
            cur_row.append(1)
            ans.append(cur_row)
        return ans
