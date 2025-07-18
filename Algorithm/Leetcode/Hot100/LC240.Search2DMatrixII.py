"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
解题思路：先按行的最小值最大值进行区间的筛选（暴力解法）、K神贪心算法
1. 我们从左下角开始搜索，获取到当前元素，然后把当前元素与45度右上角的元素进行比较，我们获得几种状态：
    * 如果我们的target小于当前元素，说明target绝对不可能在当前行，只能是前面的某行内，向上移动；
    * 如果我们的target大于当前元素，说明target可能在这一行内/上一行内，我们往右移动
"""
from typing import List


class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # 我们搜寻一下target应该在哪一行的区间内
    #     for r in range(len(matrix)):
    #         if matrix[r][0] <= target <= matrix[r][-1]:
    #             found: bool = target in matrix[r]
    #             if found:
    #                 return True
    #     return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    matrix: List[List[int]] = [
        [1, 4], [2, 5]
    ]
    print(s.searchMatrix(matrix, 4))
