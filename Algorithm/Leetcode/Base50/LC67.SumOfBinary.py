from collections import deque
from typing import Deque

"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i: int = len(a) - 1
        j: int = len(b) - 1
        # 初始化进位为 0
        carry: int = 0
        result: Deque = deque()

        while i >= 0 or j >= 0 or carry:
            # 这相当于是手动给前面补0，方便计算
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry
            # 如果total是0、1，就是自身
            # 如果total是2，变成0并且把carry置1
            # 如果total是3，变成1并且把carry置1
            result.appendleft(str(total % 2))
            carry = total // 2
            # 移动指针
            i -= 1
            j -= 1
        return "".join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11010', '1111'))