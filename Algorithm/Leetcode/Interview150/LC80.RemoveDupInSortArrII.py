from typing import List

"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
解题思路：栈
1. 由于我们不关心数组后面的数据，我们可以这样思考，不断地把需要的数据赋值到前面，直到结束；
2. 由于不能使用额外的数组空间，我们就把原来的 nums 当成栈使用。每个数字只能最多出现两次，我们这样思考，最多只有「栈顶和栈顶下方」两个数据是一样的，再出现相同的就不能入栈了；
3. 同时由于 nums 是单调递增的，我们不用担心类似这种问题 [1, 2, 1, ...]，因为此时我们会发现 nums[i] == nums[stack_head - size];
4. 那么解题思路如下：
    * 把 nums 作为栈，一开始设置栈的大小（实际上就是最多出现 K 次）为 2，然后把栈顶设置为 2（不用担心越界问题，因为如果 nums 长度 <= 2，根本不会进入循环）；
    * 维护栈顶指针是 stack_head，如果某个数字出现了 3 次及以上，那么会出现 nums[i] == nums[stack_head - size]，此时我们栈顶不变，只是增加 i 去找下一个元素；
    * 最后如果出现了重复3次以上的元素，那么 stack_head 必然会小于 len(nums)，最后返回两者中更小的即可（stack_head <= len(nums)）。
5. 这道题目如果把 stack_head 和 size 改成 1，那么也是 LC26 的解题法。
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack_head: int = 2
        size: int = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[stack_head - size]:
                nums[stack_head] = nums[i]
                stack_head += 1
        return min(stack_head, len(nums))
