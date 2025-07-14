"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans: List[int] = []
        m: int = len(matrix)
        n: int = len(matrix[0])
        marked: List[List[bool]] = [[False for _ in range(n)] for _ in range(m)]
        s_row: int = 0
        s_col: int = -1 # 为了凑循环中的状态，这里先选择-1
        # 当 marked 中还有 False 的时候，说明还要继续走
        while any(False in _ for _ in marked):
            s_row, s_col = self.goWithDirection(matrix, ans, marked, s_row, s_col + 1, dir='r')
            s_row, s_col = self.goWithDirection(matrix, ans, marked, s_row + 1, s_col, dir='d')
            s_row, s_col = self.goWithDirection(matrix, ans, marked, s_row, s_col - 1, dir='l')
            s_row, s_col = self.goWithDirection(matrix, ans, marked, s_row - 1, s_col, dir='u')
        return ans

    def goWithDirection(self, mat: List[List[int]], ans: List[int], marked: List[List[bool]], s_row: int, s_col: int,
                        dir: str) -> tuple[int, int]:
        while not marked[s_row][s_col]:
            ans.append(mat[s_row][s_col])
            marked[s_row][s_col] = True
            # 最终会停在一个位置上，返回螺旋当前位置，之后作为下一个位置输入进该函数
            if dir == 'r':
                if s_col + 1 == len(mat[0]) or marked[s_row][s_col + 1]:
                    return s_row, s_col
                s_col += 1
            elif dir == 'l':
                if s_col - 1 < 0 or marked[s_row][s_col - 1]:
                    return s_row, s_col
                s_col -= 1
            elif dir == 'u':
                if s_row - 1 < 0 or marked[s_row - 1][s_col]:
                    return s_row, s_col
                s_row -= 1
            elif dir == 'd':
                if s_row + 1 == len(mat) or marked[s_row + 1][s_col]:
                    return s_row, s_col
                s_row += 1
        return s_row, s_col


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
