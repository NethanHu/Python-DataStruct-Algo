
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
"""
from collections import deque
from typing import List, Deque


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans_list: List[str] = []
        for i in range(len(num1) - 1, -1, -1):
            carry: int = 0
            cur_mul: Deque[str] = deque()
            for j in range(len(num2) - 1, -1, -1):
                res: int = int(num1[i]) * int(num2[j]) + carry
                rem: int = res % 10
                carry = res // 10
                cur_mul.appendleft(str(rem))
            cur_mul.appendleft(str(carry) if carry != 0 else '')
            cur_mul.append('0' * (len(num1) - 1 - i))
            var: int = int(''.join(cur_mul))
            ans_list.append(str(var))
        ans: str = '0'
        for num in ans_list:
            ans = self.strSum(ans, num)
        return ans

    def strSum(self, num1: str, num2: str) -> str:
        i: int = len(num1) - 1
        j: int = len(num2) - 1
        carry: int = 0
        result: Deque[str] = deque()
        while i >= 0 or j >= 0 or carry:
            digit_a = int(num1[i]) if i >= 0 else 0
            digit_b = int(num2[j]) if j >= 0 else 0
            total = digit_a + digit_b + carry
            result.appendleft(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('9133', '0'))