from typing import List

"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        i: int = 0
        j: int = len(height) - 1
        # 1. 若向内移动短板，水槽的短板 min(h[i], h[j]) 可能变大，
        #    因此下个水槽的面积可能增大
        # 2. 若向内移动长板，水槽的短板 min(h[i], h[j]) 不变或变小，
        #    因此下个水槽的面积一定变小
        max_vol: int = 0
        while i < j:
            cur_vol: int = self.getVolumn(height, i, j)
            max_vol = max(max_vol, cur_vol)
            # 我们总是移动指向更矮那根板的指针，因为移动它才有可能让容器的“短板”变长，从而让面积增大
            if height[i] < height[j]:
                i += 1
            else:
                # 此时也包含着 height[i] == height[j] 的情况
                # 当两者相等时，不管移动哪一边，都会导致容积变小，此时为了找到最优解，我们必须移动其中一边，相当于“扰动”
                # 两边对容器高度的“限制性”是一样的。所以，无论选择移动 i 还是移动 j，对于寻找未来的最优解来说，效果是完全等价的
                j -= 1
        return max_vol

    def getVolumn(self, height: List[int], i: int, j: int) -> int:
        return (j - i) * min(height[i], height[j])


if __name__ == '__main__':
    s = Solution()
    height = [8, 7, 2, 1]
    print(s.maxArea(height))
