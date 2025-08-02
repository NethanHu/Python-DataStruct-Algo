from typing import List

"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
解题思路：Boyer-Moore 多数投票算法（找数量超过总数 1/2 的算法）
1. 如果有某个元素数量超过了总数的 1/2，我们设想一下，如果每一个元素和其他元素相互抵消，那么由于自己数量超过 1/2，必然抵消完之后剩下还会有自己存留；
2. 我们首先设置一个 votes = 0。
    * 如果在 votes = 0 的时候，我们会把当前碰到的元素设置为有可能数量超过总数 1/2 的元素；
    * 如果我们碰到了与当前「可能的答案」相同的元素，那我们就 votes += 1；如果不相同，则 -= 1。
    * 最终留下的「可能的答案」，就是我们要的答案。
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote: int = 0
        cur_num: int | None = None
        for i in range(len(nums)):
            if not cur_num or nums[i] == cur_num:
                cur_num = nums[i]
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    cur_num = None
        return cur_num
