from typing import List

"""
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
    0 <= j <= nums[i] 
    i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
解题思路：贪心算法
1. 每走一步，我们就要规划下一步要走到哪里，按照「贪心算法」的思想，要是每一步我们都是能从所有解中找出最优，那么就是整体最优，因此找到下一步最远能去哪里肯定是个全局信息；
    * 请注意，我们的小人所在的位置是 i，当前这一步最远可以抵达 cur_right，下一步最远可以抵达 next_right；
    * 怎么找下一步最远可以去哪里呢？我们在 i 的时候，把当前步长的所有格子走完，找出最大的 i + nums[i] 并且替换此时的右边界 next_right；
    * 这样当我们这一步走完的时候，即 i == cur_right，我们可以随时「回退」到这一步走到的任意格子上（我们没走回去，只是决定要从这里走），从这个格子走一步得到最新的右边界 next_right；
    * 此时 cur_right 被赋值为最远可达的 next_right，并且开始下一步寻找最优长度。
2. 细节问题，这里遍历的范围是 len(nums) - 1，否则答案会 +1。
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_right: int = 0
        next_right: int = 0
        ans_step: int = 0
        for i in range(len(nums) - 1):
            # 此时在已经搭建好的桥上面走，每到一个点都能够记下来下一步最远可以到哪里
            next_right = max(next_right, i + nums[i])
            # 如果走完了已经搭建的桥，我们开始搭下一个桥，能够到达的最远距离就是我们之前默默记录的 next_right
            if i == cur_right:
                cur_right = next_right
                # 搭建一座桥就等于跳了一步
                ans_step += 1
        return ans_step


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))