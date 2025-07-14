

"""
给定一个表示 大整数 的整数数组 digits，其中 digits[i] 是整数的第 i 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 0。
将大整数加 1，并返回结果的数字数组。
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i: int = len(digits) - 1
        if digits[i] < 9:
            digits[i] += 1
            return list(digits)
        if set(digits) == {9}:
            ans: List[int] = [1, [0] * len(digits)]
            return ans
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            i -= 1
            digits[i] += 1
        return digits

if __name__ == '__main__':
    s = Solution()
    s.plusOne([9, 9, 9])