
"""
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即x^n）。
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if x == 1.0:
            return 1.0
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n *= -1
        if x == -1.0:
            return 1.0 if n % 2 == 0 else -1.0
        ans: float = 1.0
        for i in range(n):
            ans *= x
            if abs(ans) < 10e-12:
                return 0.0
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.myPow(-1.00000, -2147483648))