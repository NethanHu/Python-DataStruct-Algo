from typing import List

"""
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
解题思路：二分查找+索引映射
1. 由于这个二维数组的特性，我们将其下一行与上一行首位相接，就可以得到一个完全递增的数组，我们就把问题转化为了在一个一维数组上进行二分查找；
    * 为了优化内存使用，我们可以不开辟一个一维数组来保存拼接后的数组；
    * 我们可以使用索引映射的方法，对于下标范围 [0, m * n - 1] 的“一维”数组中的元素，假设下标为 idx，我们可以通过 matrix[idx // n][idx % n] 这个映射找到其具体在matrix中的位置；
    * 有了这个函数，我们就可以视为直接在一个“一维”数组上进行二分查找的做法。获取到元素的方式本来为 nums[mid]，现在为 numInMatrix(mid)。
2. 开区间的二分查找思路：
    * 我们先理解一下开区间 (l, r) 的用处，l、r都是取不到具体元素的，我们要的数字只能是在 (l, r) 里面。所以只要 mid > target，由于 r 本身取不到target，因此 r = mid。
    * 我们维护一对 l，r，一开始它们是哨兵（区间外），随着算法的逐步进行，l、r 指向具体的数字，这使得它们有了意义；
    * 我们的 while 循环条件是 l + 1 < r。它的含义是：只要左哨兵 l 和右哨兵 r 之间至少还存在一个整数索引，搜索就继续。当循环结束时，
      必然有 l + 1 == r，即 l 和 r 变成了相邻的整数，它们之间的“未知区域”已经被完全挤压掉了，搜索结束；
    * 在 while 循环中我们有三个分支：
        - 如果 mid 指向的数字正好是 target，就返回 True；
        - 如果 mid 指向的数字小于 target，那说明 mid 这个左边界和它本身都是我们不感兴趣的，我们把 l 更新为 mid，那么答案只会出现在 mid 的右边；
        - 如果 mid 指向的数字大于 target，那说明 mid 这个右边界和它本身都是我们不感兴趣的，mid 之后的数字和它自己一定也是大于 target，答案只会出现在 mid 的左边。
        - 而我们先判断过 mid 指向的数字是否等于 target，这样只要不等，就说明 mid 指向的数字本身就大于 target。
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = -1, m * n

        # 我们把二维矩阵当成一个首位相接的一维矩阵看，idx就是数字的下标，通过这个函数能够定位在matrix中的位置
        def numInMatrix(idx: int) -> int:
            return matrix[idx // n][idx % n]

        while l + 1 < r:
            mid: int = (l + r) // 2
            cur_num: int = numInMatrix(mid)
            if cur_num == target:
                return True
            if cur_num < target:
                l = mid
            else:
                r = mid
        return False
