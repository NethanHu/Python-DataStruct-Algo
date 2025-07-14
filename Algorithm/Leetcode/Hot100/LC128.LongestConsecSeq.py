from typing import Set, List

"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
Hint: 在List中查找 num in num_list 是O(k)时间复杂度操作
      而在Set中查找 num in num_set 是O(1)时间复杂度，因为Set是哈希结构
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set: Set[int] = set(nums)
        max_len: int = 1
        # 如果一个数字 num 的前一个数字 num - 1 不存在于集合中，
        # 那么 num 就是一个序列的起点
        # 对于每个 num，我们先检查 num - 1 是否在集合里：
        for num in num_set:
            # 如果 num - 1 不存在，我们找到了一个序列的起点。
            if num - 1 not in num_set:
                cur_num: int = num
                cur_len = 1
                # 在这种情况我们才开始向后查找 num + 1, num + 2, ...
                # 并计算这个序列的长度
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len

