from typing import List

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
解题思路：记忆化存储
1. 我们假设这个数组全为正数，但是其中可能为0，那么我们可以轻易地得到 dp 填表公式为 max(f_max[i - 1] * x, x)：
    * 即如果出现 0，那么必然此时的最大值为连续非0数字的乘积，出现 0 的时候 dp 为 0，那么接下来新的 dp 就是再次出现的非0数，毕竟 0 * x < x；
2. 但是数组中出现负数的时候就不一样了，有可能会出现一个负数导致原本极大的乘积变成负数（此时又变成了极小的乘积）；
    * 但是如果再出现一个负数，那么这个极小的乘积又会变成极大的正数，而我们要的就是正数；
    * 因此，由于存在负数，那么会导致最大的变最小的，最小的变最大的。所以还需要维护当前最小值 f_min。
3. 我们维护当前最大值 f_max、最小值 f_min，每次比较的时候都是上一个 max、上一个 min 和当前 x 的积，同时还要与当前 x 做比较，因为可能会有 0 的出现，x 可以恢复正定性。
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n: int = len(nums)
        f_max: List[int] = [0] * n
        f_min: List[int] = [0] * n
        f_max[0] = f_min[0] = nums[0]
        for i in range(1, n):
            x: int = nums[i]
            f_max[i] = max(f_max[i - 1] * x, f_min[i - 1] * x, x)
            f_min[i] = min(f_max[i - 1] * x, f_min[i - 1] * x, x)
        return max(f_max)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
