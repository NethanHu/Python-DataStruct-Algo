from functools import reduce
from operator import xor
from typing import List

"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
解题思路：技巧
1. 异或运算符（a ^ b）能够在 a = b 的时候输出0值，同时具有结合律和交换律，因此当只有一个元素出现一次，其他所有元素都出现两次的时候，逐个进行异或运算就能输出唯一出现一次的元素；
2. 我们使用 functools 的 reduce 方法，旨在使用特定的运算符结合计算所有元素。
"""


class Solution:
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            return reduce(xor, nums)


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([2, 2, 1]))
