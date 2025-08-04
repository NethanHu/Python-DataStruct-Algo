from typing import List

"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：
更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。返回 k。
解题思路：双指针
1. 由于我们不检查最后几个的数字，因为数组的「有效」长度我们就让右指针 j 去控制，只要发现一个 val，就把 val 丢进 j 指针及右边的「垃圾场」中；
2. 双指针的逻辑如下：
    * 左指针 i 从数组的最左边开始遍历，如果指针 i 指向的数字不等于 val，那我们就让 i 右移。因为我们最终输出的长度是由 i 控制的，因此碰到不等于 val 的元素时必然让 i += 1；
    * 右指针 j 从数组的最右边开始遍历，j 只是当做「有效数组」的上限，如果左边发现了一个等于 val 的元素，就与 j 指向的元素进行交换；
        - 有可能 j 指向的元素也是 val，就会把 val 换到前面了。但是这不要紧，因为 j 会不断收窄边界，直到找到后方一个不是 val 的元素或是穿过指针 i；
        - 而指针 i 要一直等，直到换到了不是 val 的元素才会移动自己，即一直等待 j 指针「找到」合适的可更换的元素。
    * 那么最后指针 j 穿过指针 i，说明全部的数组都遍历结束，此时指针 i 就是返回的 k。
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i: int = 0
        j: int = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([2], 3))
