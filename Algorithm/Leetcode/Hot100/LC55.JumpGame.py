from typing import List

"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
解题思路：贪心算法
1. 我们只要维护一个最远可达距离 max_idx，同时遍历一遍 nums 即可。一开始 max_idx 设置为 0，即我们可以达到第 0 个位置；
2. 遍历 nums，我们有当前位置 i 和从当前出发最远距离 dist，我们进入判断：
    * 如果说 i > max_idx，即我们根本无法到达此处，就返回 False；
    * 我们根据当前得到的最远距离，去更新我们能抵达的总最远下标 max_idx，当然我们使用的是 max 函数，因为如果当前距离之和不够远，可能前者有一步可以到特别远，我们就不进行更新；
    * 最后我们有一个优化条件，如果我们可以抵达的 max_idx 已经等于或超过 len(nums) - 1，就直接返回 True。
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx: int = 0
        for i, dist in enumerate(nums):
            if i > max_idx:
                return False
            max_idx = max(max_idx, i + dist)
            # 提前返回条件
            if max_idx >= len(nums) - 1:
                return True
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
